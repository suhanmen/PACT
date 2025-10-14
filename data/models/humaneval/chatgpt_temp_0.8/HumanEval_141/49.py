def file_name_check(file_name):
    # Check for more than three digits in the file name
    digits = sum(c.isdigit() for c in file_name)
    if digits > 3:
        return 'No'
    
    # Check for exactly one dot in the file name
    dots = file_name.count('.')
    if dots != 1:
        return 'No'
    
    # Check for a valid substring before and after the dot
    name, ext = file_name.split('.')
    if not name.isalpha() or not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all conditions are met, return 'Yes'
    return 'Yes'
