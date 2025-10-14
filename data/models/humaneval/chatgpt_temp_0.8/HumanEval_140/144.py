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
    
    # replace all consecutive spaces with -
    while "--" in text:
        text = text.replace("--", "-")
    while "__" in text:
        text = text.replace("__", "_")
    while "___" in text:
        text = text.replace("___", "-")
    
    return text
