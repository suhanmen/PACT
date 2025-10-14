def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name, extension = file_name.split('.')
    if extension not in valid_extensions:
        return 'No'
    if len(name) == 0 or not name[0].isalpha():
        return 'No'
    if sum(1 for c in name if c.isdigit()) > 3:
        return 'No'
    return 'Yes'
