def file_name_check(file_name):
    import re
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9]*\.[tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL]$', file_name):
        return 'No'
    num_digits = sum(1 for c in file_name if c.isdigit())
    if num_digits > 3:
        return 'No'
    return 'Yes'
