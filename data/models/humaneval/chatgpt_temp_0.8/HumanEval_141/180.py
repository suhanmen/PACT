def file_name_check(file_name):
    digits = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    extensions = ['txt', 'exe', 'dll']
    
    if file_name.count('.') != 1:
        return 'No'
    
    file_name_split = file_name.split('.')
    if not file_name_split[0] or not file_name_split[0][0] in alphabets:
        return 'No'
    
    if not file_name_split[1] in extensions:
        return 'No'
    
    digit_count = sum(1 for c in file_name if c in digits)
    if digit_count > 3:
        return 'No'
    
    return 'Yes'
