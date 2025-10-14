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
    # replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # replace consecutive spaces with -
    i = 0
    consecutive_spaces = False
    while i < len(text)-1:
        if text[i] == " " and text[i+1] == " ":
            if not consecutive_spaces:
                consecutive_spaces = True
                text = text[:i+1] + "-" + text[i+2:]
            else:
                text = text[:i+1] + text[i+2:]
        else:
            consecutive_spaces = False
        i += 1
    
    return text
