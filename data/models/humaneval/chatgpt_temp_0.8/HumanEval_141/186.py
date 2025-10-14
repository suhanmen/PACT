def file_name_check(file_name):
    # check for number of digits
    if sum(1 for char in file_name if char.isdigit()) > 3:
        return 'No'
    # check for one dot
    if file_name.count('.') != 1:
        return 'No'
    name, ext = file_name.split('.')
    # check for empty substring before the dot
    if not name:
        return 'No'
    # check for starting letter in the substring before the dot
    if not name[0].isalpha():
        return 'No'
    # check for valid extension
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
