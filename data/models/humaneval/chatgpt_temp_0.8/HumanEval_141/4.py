def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*(\d[a-zA-Z0-9]*){0,3}\.[txt,exe,dll]{3}$'
    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'
