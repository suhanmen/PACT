def file_name_check(file_name):
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
            if digit_count > 3:
                return 'No'

    if '.' not in file_name:
        return 'No'

    file_name_parts = file_name.split('.')
    if len(file_name_parts) != 2:
        return 'No'

    file_name_prefix = file_name_parts[0]
    if not file_name_prefix or not file_name_prefix[0].isalpha():
        return 'No'

    file_extension = file_name_parts[1]
    if file_extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
