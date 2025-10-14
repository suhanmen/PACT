def file_name_check(file_name):
    digits = '0123456789'
    extensions = ['txt', 'exe', 'dll']
    
    # Check for the first condition
    digits_count = 0
    for char in file_name:
        if char in digits:
            digits_count += 1
            if digits_count > 3:
                return 'No'
    
    # Check for the second condition
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into two parts at the dot
    name, ext = file_name.split('.')
    
    # Check for the third condition
    if not name or not name[0].isalpha():
        return 'No'
    
    # Check for the fourth condition
    if ext not in extensions:
        return 'No'
    
    # All conditions are met
    return 'Yes'
