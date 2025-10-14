def file_name_check(file_name):
    if file_name.count('.') != 1:
        return 'No'
    else:
        name, extension = file_name.split('.')
        if len(extension) != 3 or extension not in ['txt', 'exe', 'dll']:
            return 'No'
        if not name[0].isalpha():
            return 'No'
        digits = 0
        for char in name:
            if char.isdigit():
                digits += 1
        if digits > 3:
            return 'No'
        return 'Yes'
