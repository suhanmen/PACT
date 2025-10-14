def file_name_check(file_name):
    if file_name.count(".") != 1:
        return "No"
    name_parts = file_name.split(".")
    if not (name_parts[0] and name_parts[0][0].isalpha()):
        return "No"
    if not (name_parts[1] in ["txt", "exe", "dll"]):
        return "No"
    if sum(1 for c in name_parts[0] if c.isdigit()) > 3:
        return "No"
    return "Yes"
