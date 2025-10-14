def file_name_check(file_name):
    digits = 0
    alpha = False
    extension = file_name.split('.')[-1]
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    before_dot = file_name.split('.')[0]
    if before_dot == '' or not before_dot[0].isalpha():
        return 'No'
    for char in before_dot:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alpha = True
        else:
            return 'No'
    if digits > 3 or not alpha:
        return 'No'
    return 'Yes'
