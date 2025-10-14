def file_name_check(file_name):
    digits = '0123456789'
    latin_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    else:
        first_part, second_part = file_name.split('.')
        if not first_part or first_part[0] not in latin_letters:
            return 'No'
        elif len([char for char in first_part if char in digits]) > 3:
            return 'No'
        elif second_part not in extensions:
            return 'No'
        else:
            return 'Yes'
