def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][\w]*\.[tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL]$'
    if re.match(pattern, file_name):
        digits_count = sum(c.isdigit() for c in file_name)
        if digits_count <= 3:
            return 'Yes'
    return 'No'
