def file_name_check(file_name):
    # check for more than three digits in file name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'
    # check for exactly one dot in file name
    if file_name.count('.') != 1:
        return 'No'
    # separate the file name into two parts: before and after the dot
    name_parts = file_name.split('.')
    name_before_dot = name_parts[0]
    name_after_dot = name_parts[1]
    # check that the substring before the dot starts with a letter
    if not name_before_dot[0].isalpha():
        return 'No'
    # check that the substring after the dot is one of ['txt', 'exe', 'dll']
    if name_after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    # if all checks pass, return 'Yes'
    return 'Yes'
