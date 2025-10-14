def file_name_check(file_name):
    if not file_name.isalnum(): # check if file_name contains only letters and numbers
        return 'No'
    if file_name.count('.') != 1: # check if there is exactly one dot in file_name
        return 'No'
    name, ext = file_name.split('.') # split file_name into name and extension
    if not name[0].isalpha(): # check if the first character of name is a letter
        return 'No'
    if not ext in ['txt', 'exe', 'dll']: # check if the extension is valid
        return 'No'
    if len([c for c in name if c.isdigit()]) > 3: # check if there are more than three digits in name
        return 'No'
    return 'Yes'
