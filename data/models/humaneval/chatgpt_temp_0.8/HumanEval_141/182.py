def file_name_check(file_name):
    digits = '0123456789'
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if extension not in valid_extensions:
        return 'No'
    if len(name) == 0 or not name[0].isalpha():
        return 'No'
    digit_count = 0
    for char in name:
        if char in digits:
            digit_count += 1
    if digit_count > 3:
        return 'No'
    return 'Yes'
