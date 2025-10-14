def file_name_check(file_name):
    if not file_name:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    file_name_parts = file_name.split('.')
    if len(file_name_parts[0]) == 0 or not file_name_parts[0][0].isalpha():
        return 'No'
    if len(file_name_parts[1]) != 3 or file_name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    digits_count = 0
    for char in file_name_parts[0]:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    return 'Yes'
