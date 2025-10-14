def file_name_check(file_name):
    import re
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    file_parts = file_name.split('.')
    if len(file_parts[0]) == 0 or not file_parts[0][0].isalpha():
        return 'No'
    if file_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
