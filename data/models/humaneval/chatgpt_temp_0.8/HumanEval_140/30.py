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
    result = ""
    consecutive_spaces = 0
    for i in range(len(text)):
        if text[i] == " ":
            if consecutive_spaces == 2:
                result = result[:-2] + "-"
            elif consecutive_spaces > 2:
                pass
            else:
                result += "_"
            consecutive_spaces += 1
        else:
            result += text[i]
            consecutive_spaces = 0
    if consecutive_spaces == 2:
        result = result[:-2] + "-"
    return result
