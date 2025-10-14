def file_name_check(file_name):
    digits = 0
    letters = 0
    dot = False
    dot_index = None
    valid_extensions = ['txt', 'exe', 'dll']
    
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits += 1
        elif file_name[i] == '.':
            if dot:
                return 'No'
            else:
                dot = True
                dot_index = i
        elif file_name[i].isalpha():
            letters += 1
    
    if digits > 3 or letters == 0 or not dot:
        return 'No'
    elif not file_name[:dot_index].isalpha() or file_name[dot_index+1:] not in valid_extensions:
        return 'No'
    else:
        return 'Yes'
