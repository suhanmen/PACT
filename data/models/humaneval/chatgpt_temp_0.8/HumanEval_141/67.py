def file_name_check(file_name):
    import re
    
    # Check if the file name contains more than three digits
    if len(re.findall('\d', file_name)) > 3:
        return 'No'
    
    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'
    
    # Check if the substring before the dot is not empty and starts with a letter from the latin alphabet
    name, extension = file_name.split('.')
    if not name or not re.match('^[A-Za-z]', name):
        return 'No'
    
    # Check if the substring after the dot is one of these: ['txt', 'exe', 'dll']
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # If all the above conditions are met, return 'Yes'
    return 'Yes'
