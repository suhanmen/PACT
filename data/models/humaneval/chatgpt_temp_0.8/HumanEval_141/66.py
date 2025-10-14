def file_name_check(file_name):
    digits_count = 0
    if file_name.count('.') != 1:
        return 'No'
    file_name_parts = file_name.split('.')
    if not file_name_parts[0] or not file_name_parts[0][0].isalpha():
        return 'No'
    for char in file_name_parts[0]:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    if file_name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
