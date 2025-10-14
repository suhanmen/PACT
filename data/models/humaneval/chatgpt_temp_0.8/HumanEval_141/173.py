def file_name_check(file_name):
    digits_count = 0
    for char in file_name:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    file_name_split = file_name.split('.')
    if len(file_name_split) != 2:
        return 'No'
    file_name_before_dot = file_name_split[0]
    file_name_after_dot = file_name_split[1]
    if len(file_name_before_dot) == 0 or not file_name_before_dot[0].isalpha():
        return 'No'
    if file_name_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
