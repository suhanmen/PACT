def file_name_check(file_name):
    import re
    pattern = "^[a-zA-Z][a-zA-Z0-9]*\.(txt|exe|dll)$"
    if re.match(pattern, file_name):
        digits_count = sum(c.isdigit() for c in file_name)
        if digits_count <= 3:
            return 'Yes'
    return 'No'
