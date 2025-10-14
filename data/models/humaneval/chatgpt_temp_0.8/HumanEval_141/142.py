def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    """
    # Check if the file name contains only valid characters
    if not file_name.isalnum() and "." in file_name and file_name.count('.') == 1:
        # Split the file name at the dot and check the validity of both substrings
        name, ext = file_name.split('.')
        if ext in ['txt', 'exe', 'dll'] and name[0].isalpha() and name.isalnum() and len([c for c in name if c.isdigit()]) <= 3:
            return 'Yes'
    return 'No'
