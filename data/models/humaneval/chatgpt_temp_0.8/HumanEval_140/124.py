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
    fixed_text = ""
    consecutive_spaces = 0
    
    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                fixed_text = fixed_text.rstrip("-")
                fixed_text += "-"
        else:
            consecutive_spaces = 0
        
        fixed_text += char if char != " " else "_" if consecutive_spaces < 3 else "-"
    
    return fixed_text.rstrip("-")
