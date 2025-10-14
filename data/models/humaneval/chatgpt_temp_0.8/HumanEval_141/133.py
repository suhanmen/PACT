def file_name_check(file_name):
    import re
    pattern = '^([a-zA-Z][a-zA-Z0-9]*)\.([tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL])$'
    if len(re.findall('[0-9]', file_name)) > 3:
        return 'No'
    elif file_name.count('.') != 1:
        return 'No'
    elif not re.match(pattern, file_name):
        return 'No'
    else:
        return 'Yes'
