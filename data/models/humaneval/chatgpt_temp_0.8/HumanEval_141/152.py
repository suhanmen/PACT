def file_name_check(file_name):
    digits = '0123456789'
    valid_extensions = ['txt', 'exe', 'dll']
    
    if file_name.count('.') != 1:
        return 'No'
    
    name, extension = file_name.split('.')
    
    if not name or name[0] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return 'No'
    
    if extension not in valid_extensions:
        return 'No'
    
    if sum(c in digits for c in file_name) > 3:
        return 'No'
    
    return 'Yes'
