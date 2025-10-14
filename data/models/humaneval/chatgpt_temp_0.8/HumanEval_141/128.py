def file_name_check(file_name):
    import re
    if re.match(r'^[a-zA-Z][a-zA-Z0-9]{0,}[.][txt|exe|dll]$', file_name):
        if len(re.findall(r'\d', file_name)) <= 3:
            return 'Yes'
    return 'No'
