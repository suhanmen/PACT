def file_name_check(file_name):
    digits_count = 0
    has_dot = False
    dot_index = None
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif file_name[i] == '.':
            if has_dot:
                return 'No'
            has_dot = True
            dot_index = i
    if not has_dot:
        return 'No'
    if dot_index == 0 or dot_index == len(file_name)-1:
        return 'No'
    if not file_name[:dot_index].isalpha():
        return 'No'
    valid_extensions = ['txt', 'exe', 'dll']
    extension = file_name[dot_index+1:]
    if extension not in valid_extensions:
        return 'No'
    return 'Yes'
