def file_name_check(file_name):
    import re
    pattern = r'^[a-zA-Z][^\.]*\.[td][xel]{2}$'
    if re.match(pattern, file_name):
        return 'Yes'
    else:
        return 'No'
