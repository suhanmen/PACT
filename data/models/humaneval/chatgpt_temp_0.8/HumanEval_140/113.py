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
    
    # Replace consecutive spaces with a single hyphen if there are more than 2 spaces
    i = 0
    hyphen_count = 0
    while i < len(text):
        if text[i] == " ":
            hyphen_count += 1
            if hyphen_count > 2:
                text = text[:i-hyphen_count+1] + "-" + text[i+1:]
        else:
            hyphen_count = 0
        i += 1
    
    return text
