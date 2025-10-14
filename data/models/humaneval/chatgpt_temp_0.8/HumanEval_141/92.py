def file_name_check(file_name):
    # check for more than three digits
    if sum(char.isdigit() for char in file_name) > 3:
        return 'No'
    
    # check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # split the file name into name and extension
    name, extension = file_name.split('.')
    
    # check the name
    if not name or not name[0].isalpha():
        return 'No'
    
    # check the extension
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
