def file_name_check(file_name):
    import re
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[txt|exe|dll]{3}$', file_name):
        if len(re.findall(r'\d', file_name)) > 3:
            return 'No'
        else:
            return 'Yes'
    else:
        return 'No'
