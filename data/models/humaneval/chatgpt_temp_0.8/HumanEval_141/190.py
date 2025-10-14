def file_name_check(file_name):
    # Check if file name contains more than three digits
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'
    
    # Check if file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split file name into parts before and after the dot
    name_parts = file_name.split('.')
    
    # Check that the part before the dot is not empty and starts with a letter from the latin alphabet
    if not name_parts[0].isalpha():
        return 'No'
    
    # Check that the part after the dot is one of the allowed extensions
    valid_extensions = ['txt', 'exe', 'dll']
    if name_parts[1] not in valid_extensions:
        return 'No'
    
    return 'Yes'
