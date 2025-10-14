def file_name_check(file_name):
    digits_count = sum(1 for char in file_name if char.isdigit())
    if digits_count > 3:
        return 'No'
    if '.' not in file_name:
        return 'No'
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'
    name, extension = name_parts
    if not name or not name[0].isalpha():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
