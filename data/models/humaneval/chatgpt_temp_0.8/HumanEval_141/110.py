def file_name_check(file_name):
    # Check if there are more than three digits in the file name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'
    
    # Check if there is exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    
    # Split the file name into two parts based on the dot
    name_parts = file_name.split('.')
    name = name_parts[0]
    extension = name_parts[1]
    
    # Check if the substring before the dot is not empty and starts with a latin alphabet letter
    if not name.isalpha() or not name[0].isalpha():
        return 'No'
    
    # Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all the conditions are met, return 'Yes'
    return 'Yes'
