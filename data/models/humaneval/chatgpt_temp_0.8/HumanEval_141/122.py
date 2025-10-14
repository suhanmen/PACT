def file_name_check(file_name):
    # check for the number of digits in the file name
    digits = [char for char in file_name if char.isdigit()]
    if len(digits) > 3:
        return 'No'

    # check for the presence of exactly one dot
    if file_name.count('.') != 1:
        return 'No'

    # check if the substring before the dot starts with a letter and is not empty
    name, ext = file_name.split('.')
    if not name[0].isalpha() or len(name) == 0:
        return 'No'

    # check if the file extension is one of the valid options
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'

    return 'Yes'
