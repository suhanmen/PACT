def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns 'Yes' if the file's name is valid, 
    and returns 'No' otherwise. A file's name is considered to be valid if and only if all the following conditions are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'.
    - The substring before the dot should not be empty, and it starts with a letter from the Latin alphabet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a Latin alphabet letter)
    """
    import re
    
    # Check if there is more than one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into two parts using the dot as the separator
    file_name_parts = file_na
