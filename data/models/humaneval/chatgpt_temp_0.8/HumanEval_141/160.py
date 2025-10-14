def file_name_check(file_name):
    num_digits = 0
    num_dots = 0
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'
    name, ext = name_parts
    if not name or not name[0].isalpha():
        return 'No'
    for c in name:
        if c.isdigit():
            num_digits += 1
    if num_digits > 3:
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
