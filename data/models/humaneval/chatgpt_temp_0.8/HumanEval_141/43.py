def file_name_check(file_name):
    import re
    regex = r"^[a-zA-Z][a-zA-Z\d]*\.[tT][xX][tT]|[eE][xX][eE]|[dD][lL][lL]$"
    if re.match(regex, file_name):
        if file_name.count('.') == 1:
            if len(file_name.split('.')[0]) > 0 and file_name.split('.')[0][0].isalpha():
                if sum(1 for c in file_name if c.isdigit()) <= 3:
                    return 'Yes'
    return 'No'
