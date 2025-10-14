def file_name_check(file_name):
    digits_count = 0
    latin_alphapet_count = 0
    file_extension = file_name.split(".")[-1]
    if file_extension not in ['txt', 'exe', 'dll']:
        return 'No'
    for i in range(len(file_name)):
        if file_name[i].isdigit():
            digits_count += 1
        elif file_name[i].isalpha():
            latin_alphapet_count += 1
            if latin_alphapet_count == 1 and not file_name[i].isalpha():
                return 'No'
        elif file_name[i] == '.':
            if i == 0 or i == len(file_name) - 1:
                return 'No'
            if digits_count > 3 or latin_alphapet_count == 0:
                return 'No'
            digits_count = 0
            latin_alphapet_count = 0
    return 'Yes'
