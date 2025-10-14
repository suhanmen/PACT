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
    while "--" in text:
        text = text.replace("--", "-")
    
    for i in range(len(text)-2):
        if text[i:i+3] == "___":
            text = text[:i] + text[i:].replace("___", "-", 1)
            break
        elif text[i:i+2] == "__":
            text = text[:i] + text[i:].replace("__", "-", 1)
            break
    
    return text
