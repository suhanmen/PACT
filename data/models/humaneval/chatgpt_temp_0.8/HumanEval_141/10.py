def file_name_check(file_name):
    # Check if there are more than three digits
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'
    
    # Check if there is exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into two parts based on the dot
    parts = file_name.split('.')
    
    # Check if the substring before the dot is valid
    if not parts[0].isalpha() or not parts[0][0].isalpha():
        return 'No'
    
    # Check if the substring after the dot is valid
    if parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'
