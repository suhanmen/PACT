def file_name_check(file_name):
    digits = "0123456789"
    valid_extensions = ["txt", "exe", "dll"]
    # Check condition 1:
    if sum(1 for char in file_name if char in digits) > 3:
        return "No"
    # Check condition 2:
    if file_name.count(".") != 1:
        return "No"
    # Check condition 3:
    name, extension = file_name.split(".")
    if not name or not name[0].isalpha():
        return "No"
    if extension not in valid_extensions:
        return "No"
    return "Yes"
