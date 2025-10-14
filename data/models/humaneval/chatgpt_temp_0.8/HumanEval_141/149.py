def file_name_check(file_name):
    digits = '0123456789'
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    if ext not in valid_extensions:
        return 'No'
    if len(name) == 0 or not name[0].isalpha():
        return 'No'
    digit_count = sum(1 for c in name if c in digits)
    if digit_count > 3:
        return 'No'
    return 'Yes'
