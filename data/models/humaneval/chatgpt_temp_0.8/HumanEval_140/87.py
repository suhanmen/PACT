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
    
    # check for consecutive spaces
    consecutive_spaces = 0
    for i in range(len(text)):
        if text[i] == " ":
            consecutive_spaces += 1
        else:
            if consecutive_spaces > 2:
                text = text[:i-consecutive_spaces] + "-" + text[i:]
            consecutive_spaces = 0
    
    # check for consecutive spaces at end
    if consecutive_spaces > 2:
        text = text[:-consecutive_spaces] + "-" * consecutive_spaces
    
    return text
