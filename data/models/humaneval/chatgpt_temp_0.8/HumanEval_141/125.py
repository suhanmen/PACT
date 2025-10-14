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
    if file_name.count(".") != 1: # if there are more than one dots
        return "No"
    name_parts = file_name.split(".")
    if not name_parts[0] or not name_parts[0][0].isalpha(): # if the substring before the dot is empty or doesn't start with a letter
        return "No"
    if name_parts[1] not in ["txt", "exe", "dll"]: # if the substring after the dot is not one of the allowed extensions
        return "No"
    if len([c for c in file_name if c.isdigit()]) > 3: # if there are more than 3 digits in the file name
        return "No"
    return "Yes"
