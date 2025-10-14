def file_name_check(file_name):
    import re
    regex = "^[a-zA-Z][a-zA-Z0-9]*(?:_[a-zA-Z0-9]+)*\.(txt|exe|dll)$"
    match = re.match(regex, file_name)
    return 'Yes' if match else 'No'
