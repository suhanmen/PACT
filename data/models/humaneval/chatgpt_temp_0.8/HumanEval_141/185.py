def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    name_parts = file_name.split('.')
    if not name_parts[0] or not name_parts[0][0].isalpha():
        return 'No'
    if len(name_parts[1]) not in [3, 4]:
        return 'No'
    if not all(char.isdigit() for char in name_parts[0]):
        return 'No'
    if name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
