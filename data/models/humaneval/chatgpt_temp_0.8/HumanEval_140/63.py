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
    text = text.replace(" ", "_") # Replace all spaces with underscores
    consecutive_spaces = 0
    previous_char = ""
    new_text = ""
    for char in text:
        if char == " ":
            consecutive_spaces += 1
        else:
            if consecutive_spaces > 2:
                new_text += "-"
            elif previous_char == " ":
                new_text += "_"
            new_text += previous_char * consecutive_spaces
            consecutive_spaces = 0
            new_text += char
        previous_char = char
    if consecutive_spaces > 2:
        new_text += "-"
    elif previous_char == " ":
        new_text += "_"
    new_text += previous_char * consecutive_spaces
    return new_text
