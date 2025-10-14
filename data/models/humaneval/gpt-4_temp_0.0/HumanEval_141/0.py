def file_name_check(file_name):
    import re

    # Check if the file name contains exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Split the file name into name and extension
    name, extension = file_name.split('.')

    # Check if the name starts with a latin alphabet letter
    if not re.match(r'^[a-zA-Z]', name):
        return 'No'

    # Check if the name contains more than three digits
    if len(re.findall(r'\d', name)) > 3:
        return 'No'

    # Check if the extension is one of the allowed extensions
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'

