def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    parts = file_name.split('.')

    # There should be exactly one dot
    if len(parts) != 2:
        return 'No'
    
    # The first part should not be empty, and it should start with a letter
    first_part = parts[0]
    if not first_part or not first_part[0].isalpha():
        return 'No'

    # Count the number of digits in the file name
    for char in file_name:
        if char.isdigit():
            digits_count += 1
    
    if digits_count > 3:
        return 'No'

    # Check if the file extension is valid
    valid_extensions = ['txt', 'exe', 'dll']
    if parts[1] not in valid_extensions:
        return 'No'

    return 'Yes'
