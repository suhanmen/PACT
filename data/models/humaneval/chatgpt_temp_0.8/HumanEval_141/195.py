def file_name_check(file_name):
    num_digits = sum(c.isdigit() for c in file_name)
    if num_digits > 3:
        return 'No'
    elif '.' not in file_name or file_name.count('.') > 1:
        return 'No'
    else:
        prefix, suffix = file_name.split('.')
        if not prefix or not prefix[0].isalpha():
            return 'No'
        elif suffix not in ['txt', 'exe', 'dll']:
            return 'No'
        else:
            return 'Yes'
