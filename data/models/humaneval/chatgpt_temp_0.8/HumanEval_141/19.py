def file_name_check(file_name):
    if file_name.count(".") != 1:
        return "No"
    else:
        name, ext = file_name.split(".")
        if len(ext) != 3 or ext not in ["txt", "exe", "dll"]:
            return "No"
        elif len([char for char in name if char.isdigit()]) > 3:
            return "No"
        elif not name[0].isalpha():
            return "No"
        else:
            return "Yes"
