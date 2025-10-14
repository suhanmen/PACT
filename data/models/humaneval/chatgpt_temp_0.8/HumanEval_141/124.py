def file_name_check(file_name):
    digits = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_extensions = ['txt', 'exe', 'dll']

    if file_name.count('.') != 1:
        return 'No'
    file_name_parts = file_name.split('.')
    if not file_name_parts[0] or not file_name_parts[0][0] in alphabets:
        return 'No'
    if len([c for c in file_name if c in digits]) > 3:
        return 'No'
    if file_name_parts[1] not in valid_extensions:
        return 'No'
    return 'Yes'
