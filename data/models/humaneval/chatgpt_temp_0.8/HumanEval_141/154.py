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
    latin_alpha = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    valid_extensions = set(['txt', 'exe', 'dll'])

    # Check that there aren't more than three digits in the file name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'

    # Split the file name into the part before the '.' and the part after the '.'
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'

    pre_dot, post_dot = parts

    # Check that the substring before the dot starts with a letter from the latin alphabet
    if not pre_dot or pre_dot[0] not in latin_alpha:
        return 'No'

    # Check that the substring after the dot is a valid extension
    if post_dot not in valid_extensions:
        return 'No'

    # If all checks pass, return 'Yes'
    return 'Yes'
