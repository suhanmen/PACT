def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    digits_count = 0
    dot_count = 0
    alpha_count = 0
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
        elif file_name[i] == '.':
            dot_count += 1
            if alpha_count == 0:
                return 'No'
        elif file_name[i].isalpha():
            alpha_count += 1
        elif not file_name[i].isalnum():
            return 'No'
    if digits_count > 3 or dot_count != 1 or alpha_count == 0:
        return 'No'
    extension = file_name.split('.')[1]
    if extension not in valid_extensions:
        return 'No'
    return 'Yes'
