def file_name_check(file_name):
    if file_name.count(".") != 1:
        return "No"
    else:
        file_name_parts = file_name.split(".")
        if len(file_name_parts[0]) == 0 or not file_name_parts[0][0].isalpha():
            return "No"
        elif file_name_parts[1] not in ['txt', 'exe', 'dll']:
            return "No"
        elif sum(c.isdigit() for c in file_name_parts[0]) > 3:
            return "No"
        else:
            return "Yes"
