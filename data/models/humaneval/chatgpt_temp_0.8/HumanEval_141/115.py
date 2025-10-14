def file_name_check(file_name):
    digits_count = 0
    if len(file_name.split(".")) != 2:
        return 'No'
    substrings = file_name.split(".")
    if not substrings[0] or not substrings[0][0].isalpha():
        return 'No'
    for char in file_name:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    if substrings[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
