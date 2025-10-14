def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*\.[txt|exe|dll]{3}$'
    if re.search(pattern, file_name):
        if len(re.findall(r'\d', file_name)) <= 3:
            return 'Yes'
    return 'No'
