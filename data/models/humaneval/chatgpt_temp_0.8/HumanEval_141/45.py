def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') != 1:
        return 'No'
    name_without_extension = file_name.split('.')[0]
    extension = file_name.split('.')[-1]
    if len(name_without_extension) == 0 or not name_without_extension[0].isalpha():
        return 'No'
    if len([char for char in name_without_extension if char.isdigit()]) > 3:
        return 'No'
    if extension not in valid_extensions:
        return 'No'
    return 'Yes'
