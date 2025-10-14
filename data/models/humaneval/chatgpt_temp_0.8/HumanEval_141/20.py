def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
        elif file_name[i] == '.':
            dot_count += 1
            if i == 0 or i == len(file_name) - 1:
                return 'No'
            if not file_name[:i].isalpha():
                return 'No'
            if not file_name[i+1:] in ['txt', 'exe', 'dll']:
                return 'No'
    if digits_count > 3 or dot_count != 1:
        return 'No'
    return 'Yes'
