def file_name_check(file_name):
    import re
    regex = r'^[a-zA-Z][\w]*\.[txt|exe|dll]{3}$'
    if re.search(regex, file_name):
        digits_count = sum(c.isdigit() for c in file_name)
        if digits_count <= 3:
            return 'Yes'
    return 'No'
