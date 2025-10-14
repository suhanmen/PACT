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
    text = text.replace(" ", "_") # replace spaces with underscores
    i = 0
    while i < len(text) - 2: # loop through the string, but not the last two characters
        if text[i:i+3] == "___": # if 3 consecutive underscores are found
            j = i+3
            while j < len(text) and text[j] == "_": # loop through consecutive underscores
                j += 1
            if j-i > 3: # if there are more than 3 consecutive underscores
                text = text[:i] + "_" + text[j:] # replace with a hyphen
            i = j
        else:
            i += 1
    return text
