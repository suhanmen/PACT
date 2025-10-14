import re

def file_name_check(file_name):
    """
    Create a function which takes a string representing a file's name, and returns 'Yes'
    if the the file's name is valid, and returns 'No' otherwise.
    """
    # The file's name contains exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    
    # The substring before the dot should not be empty, and it starts with a letter from
    # the latin alphapet ('a'-'z' and 'A'-'Z')
    file_name_parts = file_name.split('.')
    if not re.match("^[a-zA-Z]", file_name_parts[0]):
        return 'No'
    
    # The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    if file_name_parts[1] not in ['txt', 'exe', 'dll']:
        return 'No'
    
    # There should not be more than three digits ('0'-'9') in the file's name
    digits_count = sum(c.isdigit() for c in file_name_parts[0])
    if digits_count > 3:
        return 'No'
    
    # The file's name is considered to be valid if and only if all the above conditions are met
    return '
