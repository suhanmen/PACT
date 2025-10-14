def file_name_check(file_name):
    digits = "0123456789"
    extensions = ["txt", "exe", "dll"]
    
    if file_name.count(".") != 1:
        return "No"
    
    name, extension = file_name.split(".")
    
    if not name or not name[0].isalpha():
        return "No"
    
    if extension not in extensions:
        return "No"
    
    if sum(1 for c in name if c in digits) > 3:
        return "No"
    
    return "Yes"
