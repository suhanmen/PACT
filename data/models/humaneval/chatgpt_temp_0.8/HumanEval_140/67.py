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
    text = text.replace("__", "-")
    while "__" in text:
        text = text.replace("__", "-")
    
    # Replace any remaining single spaces with underscores
    text = text.replace(" ", "_")
    
    return text
