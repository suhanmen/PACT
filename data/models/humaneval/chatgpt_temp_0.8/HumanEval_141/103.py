def file_name_check(file_name):
    import re
    pattern = '^[a-zA-Z][a-zA-Z0-9]*\.(txt|exe|dll)$'
    if re.match(pattern, file_name) and len(re.findall('[0-9]', file_name)) <= 3:
        return 'Yes'
    else:
        return 'No'
