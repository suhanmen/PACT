def file_name_check(file_name):
    import re
    if not re.match('^[a-zA-Z][a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)*\.(txt|exe|dll)$', file_name):
        return 'No'
    if len(re.findall('\d', file_name)) > 3:
        return 'No'
    return 'Yes'
