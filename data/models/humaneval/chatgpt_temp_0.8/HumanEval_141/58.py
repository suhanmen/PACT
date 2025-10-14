def file_name_check(file_name):
    digit_count = 0
    dot_count = 0
    
    for i, char in enumerate(file_name):
        if char.isdigit():
            digit_count += 1
            if digit_count > 3:
                return 'No'
        elif char == '.':
            dot_count += 1
            if dot_count > 1:
                return 'No'
        elif i == 0 or (i == 1 and file_name[0] == '.') or (i == len(file_name) - 1 and char == '.'):
            return 'No'
        elif not char.isalpha() and not char.isdigit():
            return 'No'
    
    if dot_count == 1 and file_name.split('.')[1] in ['txt', 'exe', 'dll']:
        return 'Yes'
    else:
        return 'No'
