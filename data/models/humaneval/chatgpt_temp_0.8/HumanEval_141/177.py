def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if len(extension) != 3 or extension not in valid_extensions:
        return 'No'
    
    if len(name) - len(name.lstrip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')) != 1:
        return 'No'
    
    if name.count('.') != 0 or len(name) - len(''.join(filter(str.isdigit, name))) > 3:
        return 'No'
    
    return 'Yes'
