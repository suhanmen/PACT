def file_name_check(file_name):
    # Check for more than three digits in the file's name
    if sum(1 for c in file_name if c.isdigit()) > 3:
        return 'No'

    # Check for exactly one dot in the file's name
    if file_name.count('.') != 1:
        return 'No'

    # Split the file's name into two substrings based on the dot
    name_parts = file_name.split('.')
    if len(name_parts) != 2:
        return 'No'

    # Check the first substring
    first_part = name_parts[0]
    if not first_part or not first_part[0].isalpha():
        return 'No'

    # Check the second substring
    second_part = name_parts[1]
    if second_part not in ['txt', 'exe', 'dll']:
        return 'No'

    # If we reach this point, the file name is valid
    return 'Yes'
