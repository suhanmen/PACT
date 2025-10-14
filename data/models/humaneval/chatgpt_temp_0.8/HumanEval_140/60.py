def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with -
    """
    # Replace all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replace consecutive spaces with a single hyphen if there are more than 2
    while "--" in text:
        text = text.replace("--", "-")
    text = text.replace("  ", "-")
    text = text.replace("__", "_")
    
    # If the first character is a space, replace it with an underscore
    if text.startswith(" "):
        text = "_" + text[1:]
    
    # If the last character is a space, replace it with an underscore
    if text.endswith(" "):
        text = text[:-1] + "_"
    
    return text
