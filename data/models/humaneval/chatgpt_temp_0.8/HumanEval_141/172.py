def file_name_check(file_name):
    import re
    valid_extensions = ['txt', 'exe', 'dll']
    if len(re.findall('\d', file_name)) > 3 or file_name.count('.') != 1:
        return 'No'
    file_name_parts = file_name.split('.')
    if not file_name_parts[0] or not file_name_parts[0][0].isalpha() or file_name_parts[1] not in valid_extensions:
        return 'No'
    return 'Yes'
