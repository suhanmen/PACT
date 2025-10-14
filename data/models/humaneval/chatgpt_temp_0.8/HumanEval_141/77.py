def file_name_check(file_name):
    # Check for more than three digits
    if sum(char.isdigit() for char in file_name) > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Check for valid prefix and suffix
    prefix, suffix = file_name.split('.')
    if not prefix or not prefix[0].isalpha():
        return 'No'
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
