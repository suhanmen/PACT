def file_name_check(file_name):
    digits_count = 0
    for c in file_name:
        if c.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    name, ext = parts
    if not name or not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
