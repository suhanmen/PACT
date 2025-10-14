def file_name_check(file_name):
    # Check for more than three digits
    if sum(char.isdigit() for char in file_name) > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Check for substring before dot starting with a letter from the latin alphabet
    file_name_parts = file_name.split('.')
    if not file_name_parts[0].isalpha():
        return 'No'
    
    # Check for substring after dot being one of ['txt', 'exe', 'dll']
    if file_name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
