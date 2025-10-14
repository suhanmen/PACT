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
    result = []
    counter = 0
    for char in text:
        if char == " ":
            counter += 1
            if counter > 2:
                continue
            result.append("_")
        else:
            counter = 0
            result.append(char)
    result = "".join(result)
    result = result.replace("__", "-")
    return result
