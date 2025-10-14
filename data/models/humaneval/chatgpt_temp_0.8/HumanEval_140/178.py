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
    if not text:
        return text
    
    new_text = ""
    consecutive_spaces_count = 0
    
    for i, char in enumerate(text):
        if char == " ":
            consecutive_spaces_count += 1
            if consecutive_spaces_count == 3:
                new_text += "-"
                consecutive_spaces_count = 0
        else:
            if consecutive_spaces_count > 0:
                new_text += "_"
                consecutive_spaces_count = 0
            new_text += char
            
    return new_text
