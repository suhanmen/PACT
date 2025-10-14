def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    dot_index = None
    file_ext = None

    for i, c in enumerate(file_name):
        if c.isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif c == '.':
            dot_count += 1
            if dot_count > 1:
                return 'No'
            dot_index = i
            file_ext = file_name[dot_index+1:]
        elif not c.isalpha():
            return 'No'

    if dot_count != 1 or dot_index == 0 or dot_index == len(file_name)-1:
        return 'No'
    elif file_ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
