def file_name_check(file_name):
    # Check for more than three digits in the file name
    if sum(c.isdigit() for c in file_name) > 3:
        return 'No'
    
    # Check for exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into filename and extension
    filename, extension = file_name.split('.')
    
    # Check that filename is not empty and starts with a letter
    if not filename or not filename[0].isalpha():
        return 'No'
    
    # Check that the extension is valid
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all checks pass, return 'Yes'
    return 'Yes'
