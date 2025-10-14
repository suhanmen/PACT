def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    valid_extensions = ['txt', 'exe', 'dll']
    if file_name.count('.') == 1:
        dot_index = file_name.index('.')
        if dot_index > 0 and dot_index < len(file_name) - 1:
            for i in range(dot_index + 1, len(file_name)):
                if file_name[i:].lower() in valid_extensions:
                    if digits_count <= 3:
                        return 'Yes'
                    else:
                        return 'No'
                elif file_name[i].isdigit():
                    digits_count += 1
                else:
                    return 'No'
        else:
            return 'No'
    else:
        return 'No'
