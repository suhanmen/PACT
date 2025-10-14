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
    spaces_count = 0
    for char in text:
        if char == " ":
            spaces_count += 1
            if spaces_count > 2:
                fixed_text += "-"
            else:
                fixed_text += "_"
        else:
            spaces_count = 0
            fixed_text += char
    return fixed_text
