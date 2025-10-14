def file_name_check(file_name):
    import re
    regex = re.compile('[^0-9a-zA-Z]')
    file_name = regex.sub('', file_name)
    if len(re.findall('[0-9]', file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    filename, extension = file_name.split('.')
    if not filename.isalpha() or not filename[0].isalpha():
        return 'No'
    if extension not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'
