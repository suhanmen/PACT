def file_name_check(file_name):
    digits_count = 0
    for c in file_name:
        if c.isdigit():
            digits_count += 1
    if digits_count > 3 or '.' not in file_name or file_name.count('.') != 1:
        return 'No'
    parts = file_name.split('.')
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
