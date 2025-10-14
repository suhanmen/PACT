def file_name_check(file_name):
    digits_count = 0
    dot_count = 0
    valid_extensions = ['txt', 'exe', 'dll']
    file_name_parts = file_name.split('.')
    
    # Check if there is exactly one dot in the file's name
    if len(file_name_parts) != 2:
        return 'No'
    
    # Check if the substring before the dot starts with a letter from the latin alphabet
    if not file_name_parts[0].isalpha():
        return 'No'
    
    # Check if the substring after the dot is a valid extension
    if file_name_parts[1] not in valid_extensions:
        return 'No'
    
    # Count the number of digits in the file's name
    for char in file_name_parts[0]:
        if char.isdigit():
            digits_count += 1
    if digits_count > 3:
        return 'No'
    
    # If all checks have passed, return 'Yes'
    return 'Yes'
