def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    for i, c in enumerate(file_name):
        if c.isdigit():
            digits_count += 1
        elif c == '.':
            dot_count += 1
            dot_index = i
    if digits_count <= 3 and dot_count == 1:
        name_part = file_name[:dot_index]
        ext_part = file_name[dot_index+1:]
        if name_part.isalpha() and ext_part in ['txt', 'exe', 'dll']:
            return 'Yes'
    return 'No'
