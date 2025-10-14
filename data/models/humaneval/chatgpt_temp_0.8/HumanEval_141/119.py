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
    if file_name.count('.') != 1: # check if there is exactly one dot
        return 'No'
    else:
        name, extension = file_name.split('.') # split the name and extension
        if not name or not name[0].isalpha(): # check if the name is not empty and starts with a letter
            return 'No'
        elif extension not in ['txt', 'exe', 'dll']: # check if the extension is valid
            return 'No'
        elif sum(c.isdigit() for c in name) > 3: # check if there are not more than 3 digits in the name
            return 'No'
        else:
            return 'Yes'
