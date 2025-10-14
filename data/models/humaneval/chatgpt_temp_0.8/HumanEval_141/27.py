def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    for i, c in enumerate(file_name):
        if c.isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif c == '.':
            dot_count += 1
            if dot_count > 1 or i == 0:
                return 'No'
            file_ext = file_name[i+1:]
            if file_ext not in ['txt', 'exe', 'dll']:
                return 'No'
        elif not c.isalpha():
            return 'No'
    return 'Yes'
