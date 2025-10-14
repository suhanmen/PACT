def file_name_check(file_name):
    import re
    
    # Check if the file name contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9]+\.[txt|exe|dll]{3}$', file_name):
        return 'No'
    
    # Check the number of digits in the file name
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    
    # Check the substring before the dot
    file_name_parts = file_name.split('.')
    if len(file_name_parts) != 2 or not file_name_parts[0].isalpha():
        return 'No'
    
    return 'Yes'
