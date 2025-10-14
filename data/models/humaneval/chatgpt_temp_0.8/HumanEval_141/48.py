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

    # Check for more than three digits in the file's name
    digits = sum([1 for char in file_name if char.isdigit()])
    if digits > 3:
        return 'No'

    # Check for exactly one dot in the file's name
    dots = [i for i, char in enumerate(file_name) if char == '.']
    if len(dots) != 1:
        return 'No'

    # Check the substring before the dot starts with a letter from the latin alphabet
    before_dot = file_name[:dots[0]]
    if not before_dot[0].isalpha():
        return 'No'

    # Check the substring after the dot is one of ['txt', 'exe', 'dll']
    after_dot = file_name[dots[0] + 1:]
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
