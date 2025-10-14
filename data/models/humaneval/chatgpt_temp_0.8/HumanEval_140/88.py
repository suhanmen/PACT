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
    new_text = text.replace(" ", "_")
    
    # Replace consecutive spaces with -
    i = 0
    while i < len(new_text)-2:
        if new_text[i:i+3] == "___":
            # replace all consecutive spaces with -
            new_text = new_text[:i] + "-" + new_text[i+3:]
        else:
            i += 1
    return new_text
