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
    space_count = 0
    
    for char in text:
        if char == " ":
            space_count += 1
            if space_count == 1 or space_count == 2:
                fixed_text += "_"
            elif space_count > 2:
                fixed_text += "-"
        else:
            space_count = 0
            fixed_text += char
    
    return fixed_text
