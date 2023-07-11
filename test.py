import json


def extract_json_substring(string):
    # Find the first occurrence of a curly brace '{' or square bracket '['

    if string.find('{') == -1 and string.find('[') == -1:
        return ''
    if string.find('{') == -1:
        start_index = string.find('[')
    elif string.find('[') == -1:
        start_index = string.find('{')
    else:
        start_index = min(string.find('{'), string.find('['))
    print(start_index)
    if start_index == -1:
        # No opening brace or bracket found, return None
        return None

    # Track the number of opening and closing braces/brackets encountered
    count = 1
    end_index = start_index + 1

    while end_index < len(string):
        if string[end_index] == '{' or string[end_index] == '[':
            count += 1
        elif string[end_index] == '}' or string[end_index] == ']':
            count -= 1

        if count == 0:
            # Found matching closing brace or bracket, extract the JSON substring
            json_substring = string[start_index:end_index + 1]

            try:
                # Validate if the substring is a valid JSON
                json.loads(json_substring)
                return json_substring
            except json.JSONDecodeError:
                # Invalid JSON, continue searching for another substring
                pass

        end_index += 1

    # No valid JSON substring found, return None
    return ''


print(extract_json_substring(
    'Output :{"name":"John", "age":30, "city":"New York" }'))
