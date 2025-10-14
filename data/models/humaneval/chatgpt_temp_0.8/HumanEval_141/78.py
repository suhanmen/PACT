def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][\w]*\.[txt|exe|dll]{3}$'
    if re.match(pattern, file_name):
        digits_count = sum(char.isdigit() for char in file_name)
        if digits_count <= 3:
            return 'Yes'
    return 'No'
