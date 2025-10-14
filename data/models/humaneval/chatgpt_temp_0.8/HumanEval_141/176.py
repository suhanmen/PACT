def file_name_check(file_name):
    import re
    # Check for more than three digits
    if len(re.findall(r'\d', file_name)) > 3:
        return 'No'
    # Check for exactly one dot '.'
    if file_name.count('.') != 1:
        return 'No'
    # Check for substring before dot
    name, ext = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    # Check for substring after dot
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
