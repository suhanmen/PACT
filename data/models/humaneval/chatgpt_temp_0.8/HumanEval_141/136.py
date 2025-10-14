def file_name_check(file_name):
    # Check for more than three digits
    digits = [char for char in file_name if char.isdigit()]
    if len(digits) > 3:
        return 'No'
    
    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Check substring before the dot
    name_parts = file_name.split('.')
    before_dot = name_parts[0]
    after_dot = name_parts[1]
    if not before_dot.isalpha() or len(before_dot) == 0:
        return 'No'
    
    # Check substring after the dot
    if after_dot not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
