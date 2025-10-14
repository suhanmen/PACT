def file_name_check(file_name):
    # Check the number of digits in the file name
    num_digits = sum(1 for char in file_name if char.isdigit())
    if num_digits > 3:
        return 'No'

    # Check for exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # Check the substring before the dot
    name, ext = file_name.split('.')
    if len(name) == 0 or not name[0].isalpha():
        return 'No'

    # Check the substring after the dot
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
