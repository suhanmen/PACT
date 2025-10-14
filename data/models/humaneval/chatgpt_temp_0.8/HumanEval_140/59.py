def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.replace(" ", "_")  # replace spaces with underscores
    lst = list(text)  # convert string to list
    for i in range(2, len(lst)):
        if lst[i] == "_" and lst[i-1] == "_" and lst[i-2] == "_":
            # if three consecutive underscores are found
            for j in range(i, len(lst)):
                if lst[j] != "_":
                    break
                lst[j] = "-"  # replace consecutive underscores with a hyphen
    text = "".join(lst)  # convert list back to string
    return text
