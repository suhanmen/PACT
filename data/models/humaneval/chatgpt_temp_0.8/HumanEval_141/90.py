def file_name_check(file_name):
    # Check for more than three digits
    if sum(char.isdigit() for char in file_name) > 3:
        return "No"
    
    # Check for exactly one dot
    if file_name.count(".") != 1:
        return "No"
    
    # Split the file name into two parts
    name, extension = file_name.split(".")
    
    # Check for non-empty substring before the dot, starting with a letter
    if not name or not name[0].isalpha():
        return "No"
    
    # Check for valid extension
    if extension not in ["txt", "exe", "dll"]:
        return "No"
    
    return "Yes"
