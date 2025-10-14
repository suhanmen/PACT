def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    dot_index = None
    file_extension = None

    for i, char in enumerate(file_name):
        if char.isdigit():
            digits_count += 1
        elif char == '.':
            dot_count += 1
            dot_index = i

    if digits_count > 3 or dot_count != 1 or dot_index == 0 or dot_index == len(file_name) - 1:
        return 'No'

    file_extension = file_name[dot_index+1:]
    if file_extension not in ['txt', 'exe', 'dll']:
        return 'No'

    for char in file_name[:dot_index]:
        if not char.isalpha():
            return 'No'

    return 'Yes'
