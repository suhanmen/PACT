def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    dot_index = -1
    for i, c in enumerate(file_name):
        if c.isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif c == '.':
            dot_count += 1
            dot_index = i
            if dot_count > 1:
                return 'No'
        elif not c.isalpha():
            return 'No'
    if dot_count != 1:
        return 'No'
    file_extension = file_name[dot_index+1:]
    if file_extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
