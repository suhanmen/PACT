def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    dot_index = -1
    for i in range(len(file_name)):
        if file_name[i] == '.':
            dot_count += 1
            dot_index = i
        elif file_name[i].isdigit():
            digits_count += 1
    if digits_count > 3 or dot_count != 1 or dot_index == 0 or dot_index == len(file_name) - 1:
        return 'No'
    if file_name[0].isalpha() and file_name[dot_index+1:] in ['txt', 'exe', 'dll']:
        return 'Yes'
    return 'No'
