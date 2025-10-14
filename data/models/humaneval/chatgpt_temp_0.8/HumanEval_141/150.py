def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][a-zA-Z0-9]*\.[txe][txe]?[txe]?$'
    if re.match(pattern, file_name):
        digits = sum(c.isdigit() for c in file_name)
        if digits <= 3:
            return 'Yes'
    return 'No'
