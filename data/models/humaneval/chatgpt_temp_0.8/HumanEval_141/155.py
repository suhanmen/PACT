def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    digits_count = 0
    dot_count = 0

    for i, char in enumerate(file_name):
        if char.isdigit():
            digits_count += 1
            if digits_count > 3:
                return 'No'
        elif char == '.':
            dot_count += 1
            if dot_count > 1:
                return 'No'
            extension = file_name[i+1:]
            if extension not in valid_extensions:
                return 'No'
        elif i == 0 and not char.isalpha():
            return 'No'
        elif char == ' ':
            return 'No'
        
    if dot_count == 1 and digits_count <= 3:
        return 'Yes'
    else:
        return 'No'
