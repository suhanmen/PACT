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
    text = text.strip() # removes whitespace from beginning and end of string
    
    # replaces all spaces with underscores
    text = text.replace(" ", "_")
    
    # replaces consecutive spaces with a single dash if there are more than 2 consecutive spaces
    while "--" in text:
        text = text.replace("--", "-")
    if "   " in text:
        text = text.replace("   ", "-")
        text = text.replace(" ", "_")
        text = "_" + text
    
    return text
