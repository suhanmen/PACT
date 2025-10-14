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
    text = text.replace(" ", "_")  # replace spaces with underscores
    i = 0
    while i < len(text) - 2:  # loop until the third to last character
        if text[i] == "_" and text[i+1] == "_" and text[i+2] == "_":  # check for consecutive underscores
            j = i + 3
            while j < len(text) and text[j] == "_":  # loop to find how many consecutive underscores there are
                j += 1
            text = text[:i] + "-" + text[j:]  # replace consecutive underscores with a hyphen
        else:
            i += 1
    return text
