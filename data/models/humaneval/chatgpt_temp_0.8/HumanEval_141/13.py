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
    import re
    
    pattern = r"^[a-zA-Z][\w]*\.[tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL]$"
    
    if len(re.findall(r"\d", file_name)) <= 3:
        if file_name.count(".") == 1:
            prefix, suffix = file_name.split(".")
            if prefix and re.match(r"^[a-zA-Z]", prefix) and re.match(pattern, suffix):
                return 'Yes'
    return 'No'
