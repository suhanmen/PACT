def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*\.(txt|exe|dll)$'
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif not re.match(pattern, file_name):
        return 'No'
    else:
        return 'Yes'
