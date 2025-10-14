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
    # Replace all single spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace consecutive spaces with -
    i = 0
    while i < len(text) - 2:
        if text[i] == " " and text[i+1] == " " and text[i+2] == " ":
            text = text[:i] + "_" + text[i+3:]
            j = i+1
            while j < len(text) and text[j] == " ":
                j += 1
            text = text[:i+1] + "-" + text[j:]
        i += 1
    
    return text
