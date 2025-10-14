import re

def file_name_check(file_name):
    # Check if there are more than three digits in the file's name
    digit_count = len(re.findall(r'\d', file_name))
    if digit_count > 3:
        return 'No'
    
    # Check if the file's name contains exactly one dot
    dot_count = len(re.findall(r'\.', file_name))
    if dot_count != 1:
        return 'No'
    
    # Split the file's name into two parts by the dot
    parts = file_name.split('.')
    if len(parts) != 2:
        return 'No'
    
    # Check if the substring before the dot is valid
    prefix = parts[0]
    if len(prefix) == 0 or not prefix[0].isalpha():
        return 'No'
    
    # Check if the substring after the dot is valid
    suffix = parts[1]
    if suffix not in ['txt', 'exe', 'dll']:
        return 'No'
    
    return 'Yes'
