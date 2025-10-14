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
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    allowed_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    else:
        name_parts = file_name.split('.')
        if len(name_parts[0]) == 0 or name_parts[0][0] not in letters:
            return 'No'
        elif name_parts[1] not in allowed_extensions:
            return 'No'
        else:
            num_digits = sum([1 for char in name_parts[0] if char in digits])
            if num_digits > 3:
                return 'No'
            else:
                return 'Yes'
