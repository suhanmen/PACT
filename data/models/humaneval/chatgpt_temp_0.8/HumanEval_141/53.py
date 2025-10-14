def file_name_check(file_name):
    digits_count = 0
    for char in file_name:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    if '.' not in file_name:
        return 'No'
    name, extension = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
