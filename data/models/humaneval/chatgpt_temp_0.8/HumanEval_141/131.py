def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    num_digits = 0
    num_dots = 0
    alphabetic_found = False
    
    # Check all characters in the file name
    for c in file_name:
        # Count digits
        if c.isdigit():
            num_digits += 1
            if num_digits > 3:
                return 'No'
        # Count dots
        elif c == '.':
            num_dots += 1
            if num_dots > 1:
                return 'No'
        # Check if alphabetic character is found
        elif c.isalpha():
            alphabetic_found = True
    
    # Check if the file name meets all conditions
    if num_dots != 1 or not alphabetic_found:
        return 'No'
    else:
        extension = file_name.split('.')[-1]
        if extension not in valid_extensions:
            return 'No'
    
    return 'Yes'
