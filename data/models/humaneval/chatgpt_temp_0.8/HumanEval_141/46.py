def file_name_check(file_name):
    import re
    digits = re.findall('\d', file_name)
    if len(digits) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    else:
        parts = file_name.split('.')
        if not parts[0].isalpha():
            return 'No'
        elif parts[1] not in ['txt', 'exe', 'dll']:
            return 'No'
        else:
            return 'Yes'
