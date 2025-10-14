def file_name_check(file_name):
    digits = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name_parts = file_name.split('.')
    if not name_parts[0] or not name_parts[0][0] in alphabets:
        return 'No'
    if not name_parts[1] in valid_extensions:
        return 'No'
    if sum(1 for c in file_name if c in digits) > 3:
        return 'No'
    return 'Yes'
