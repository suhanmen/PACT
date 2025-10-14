def file_name_check(file_name):
    digits = 0
    for char in file_name:
        if char.isdigit():
            digits += 1
    if digits > 3:
        return "No"
    if file_name.count('.') != 1:
        return "No"
    file_parts = file_name.split('.')
    if not file_parts[0][0].isalpha():
        return "No"
    if file_parts[1] not in ['txt', 'exe', 'dll']:
        return "No"
    return "Yes"
