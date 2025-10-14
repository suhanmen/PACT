def file_name_check(file_name):
    num_digits = 0
    has_dot = False
    dot_index = -1
    
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            num_digits += 1
            if num_digits > 3:
                return 'No'
        elif file_name[i] == '.':
            if has_dot:
                return 'No'
            else:
                has_dot = True
                dot_index = i
        elif not file_name[i].isalpha():
            return 'No'
    
    if not has_dot or dot_index == 0 or dot_index == len(file_name) - 1:
        return 'No'
    
    ext = file_name[dot_index+1:]
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
