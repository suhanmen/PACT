def file_name_check(file_name):
    # check for number of digits
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'
    # check for one dot
    if file_name.count('.') != 1:
        return 'No'
    # get the substrings before and after the dot
    parts = file_name.split('.')
    if len(parts[0]) == 0 or not parts[0][0].isalpha():
        return 'No'
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
