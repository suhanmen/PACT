def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name_parts = file_name.split('.')
    if not name_parts[0].isalpha() or len(name_parts[0]) == 0:
        return 'No'
    if len([c for c in name_parts[0] if c.isdigit()]) > 3:
        return 'No'
    if name_parts[1] not in valid_extensions:
        return 'No'
    return 'Yes'
