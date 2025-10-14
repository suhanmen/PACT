def file_name_check(file_name):
    dots = file_name.count('.')
    if dots != 1:
        return 'No'
    else:
        name, extension = file_name.split('.')
        if extension not in ['txt', 'exe', 'dll']:
            return 'No'
        if not name[0].isalpha():
            return 'No'
        digit_count = sum([1 for char in name if char.isdigit()])
        if digit_count > 3:
            return 'No'
        else:
            return 'Yes'
