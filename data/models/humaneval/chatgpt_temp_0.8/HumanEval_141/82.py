def file_name_check(file_name):
    digits_count = 0
    dot_index = file_name.find('.')
    if dot_index == -1 or dot_index == 0 or dot_index == len(file_name) - 1:
        return 'No'
    for i in range(dot_index + 1, len(file_name)):
        if file_name[i:i + 3] == 'txt' or file_name[i:i + 3] == 'exe' or file_name[i:i + 3] == 'dll':
            if i + 3 == len(file_name):
                break
            else:
                return 'No'
    for i in range(dot_index):
        if not file_name[i].isalpha():
            return 'No'
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
        if digits_count > 3:
            return 'No'
    return 'Yes'
