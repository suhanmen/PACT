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
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace all consecutive spaces with -
    i = 0
    while i < len(text) - 2:
        if text[i] == " " and text[i+1] == " " and text[i+2] == " ":
            text = text[:i] + "-" + text[i+3:]
        else:
            i += 1
            
    # Return the modified text
    return text
