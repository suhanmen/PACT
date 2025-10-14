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
    text = text.replace(" ", "_") # Replace all spaces with underscores
    i = 0
    while i < len(text)-2:
        if text[i:i+3] == "___": # Check for 3 consecutive underscores
            j = i+3
            while j < len(text) and text[j] == "_":
                j += 1
            text = text[:i] + "_" + text[j:] # Replace consecutive underscores with hyphen
        i += 1
    return text
