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
    text = text.replace(" ", "_") # replace all spaces with underscores
    i = 0
    count = 0
    while i < len(text):
        if text[i] == " ":
            count += 1
        else:
            if count > 2:
                text = text[:i-count] + "-" + text[i:]
            count = 0
        i += 1
    if count > 2:
        text = text[:i-count] + "-" # replace consecutive spaces with -
    return text
