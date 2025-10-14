def file_name_check(file_name):
    # Check for more than three digits in the name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'

    # Check for exactly one dot in the name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the name into substrings
    parts = file_name.split('.')
    
    # Check that the substring before the dot is valid
    if not parts[0] or not parts[0][0].isalpha():
        return 'No'
    
    # Check that the substring after the dot is valid
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all checks pass, the name is valid
    return 'Yes'
