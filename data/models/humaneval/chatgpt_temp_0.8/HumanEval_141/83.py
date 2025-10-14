def file_name_check(file_name):
    if not file_name:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    digit_count = sum(1 for char in name if char.isdigit())
    if digit_count > 3:
        return 'No'
    return 'Yes'
