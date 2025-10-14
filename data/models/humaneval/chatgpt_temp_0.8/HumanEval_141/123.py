def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """

    # check if there are more than three digits in the file name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'

    # check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'

    # split the file name into two parts, before and after the dot
    name_parts = file_name.split('.')
    before_dot = name_parts[0]
    after_dot = name_parts[1]

    # check if the substring before the dot is empty or does not start with a letter
    if not before_dot.isalpha() or len(before_dot) == 0:
        return 'No'

    # check if the substring after the dot is valid
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
