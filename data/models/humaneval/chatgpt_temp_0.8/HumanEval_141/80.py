def file_name_check(file_name):
    digits = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valid_extensions = ['txt', 'exe', 'dll']
    dot_count = file_name.count('.')
    if dot_count == 1:
        name, extension = file_name.split('.')
        if len(name) > 0 and name[0] in alphabets and extension in valid_extensions and len([char for char in name if char in digits]) <= 3:
            return 'Yes'
    return 'No'
