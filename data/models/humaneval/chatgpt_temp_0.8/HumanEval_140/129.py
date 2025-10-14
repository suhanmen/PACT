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
    fixed_text = text.replace(" ", "_") # replace all spaces with underscores
    
    i = 0
    while i < len(fixed_text):
        if fixed_text[i:i+3] == "___":
            fixed_text = fixed_text[:i] + fixed_text[i:].replace(" ", "-", 1) # replace consecutive spaces with -
        i += 1
    
    return fixed_text
