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
    prev_space = False
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            if prev_space:
                consecutive_spaces += 1
            else:
                prev_space = True
                consecutive_spaces = 1
                
            if consecutive_spaces > 2:
                result = result[:-1] + "-"
        else:
            prev_space = False
            consecutive_spaces = 0
            
        result += char if char != " " else "_"
    
    return result
