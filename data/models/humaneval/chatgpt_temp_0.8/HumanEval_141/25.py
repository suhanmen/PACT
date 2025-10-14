def file_name_check(file_name):
    import re
    if re.match(r'^[a-zA-Z][\w]*\.\w{3}$', file_name):
        return 'Yes'
    else:
        return 'No'
