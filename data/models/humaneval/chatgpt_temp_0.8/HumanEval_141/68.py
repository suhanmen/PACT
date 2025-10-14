def file_name_check(file_name):
    # check for more than three digits in file name
    digit_count = 0
    for char in file_name:
        if char.isdigit():
            digit_count += 1
    if digit_count > 3:
        return 'No'

    # check for exactly one dot in file name
    dot_count = 0
    for char in file_name:
        if char == '.':
            dot_count += 1
    if dot_count != 1:
        return 'No'

    # check for valid prefix and suffix
    prefix, suffix = file_name.split('.')
    if not prefix or not prefix[0].isalpha():
        return 'No'
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'

    # if all checks pass, return 'Yes'
    return 'Yes'
