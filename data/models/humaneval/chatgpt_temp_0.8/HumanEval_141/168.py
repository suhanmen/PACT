def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns 'Yes'
    if the file's name is valid, and returns 'No' otherwise. A file's name is considered
    to be valid if and only if all the following conditions are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    """
    import re
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*\.(txt|exe|dll)$'
    return 'Yes' if re.match(pattern, file_name) and len(re.findall(r'\d', file_name)) <= 3 else 'No'
