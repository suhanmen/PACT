def file_name_check(file_name):
    digits_count = 0
    for char in file_name:
        if char.isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif not char.isalpha() and char != '.':
            return 'No'
    if digits_count == 0 or '.' not in file_name:
        return 'No'
    file_parts = file_name.split('.')
    if len(file_parts) != 2 or file_parts[0] == '' or not file_parts[0][0].isalpha():
        return 'No'
    if file_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
