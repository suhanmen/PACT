def file_name_check(file_name):
    digits = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    extensions = ['txt', 'exe', 'dll']

    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    if not name or not name[0] in alphabets:
        return 'No'
    if ext not in extensions:
        return 'No'
    if len([char for char in name if char in digits]) > 3:
        return 'No'

    return 'Yes'
