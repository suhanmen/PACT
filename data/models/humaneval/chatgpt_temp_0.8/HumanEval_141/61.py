def file_name_check(file_name):
    valid_extensions = ['txt', 'exe', 'dll']
    # Check for exactly one dot in the file name
    if file_name.count('.') != 1:
        return 'No'
    else:
        # Split file name into substring before and after the dot
        name, extension = file_name.split('.')
        # Check that the substring before the dot is not empty and starts with a letter
        if not name or not name[0].isalpha():
            return 'No'
        # Check that the substring after the dot is one of the valid extensions
        elif extension not in valid_extensions:
            return 'No'
        # Check for no more than three digits in the file name
        elif sum(1 for c in name if c.isdigit()) > 3:
            return 'No'
        else:
            return 'Yes'
