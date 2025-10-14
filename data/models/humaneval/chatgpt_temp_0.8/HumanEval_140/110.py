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
    # Replacing all spaces with underscores
    text = text.replace(" ", "_")
    
    # Replacing consecutive spaces with -
    count = 0
    new_text = ""
    for i in range(len(text)):
        if text[i] == " ":
            count += 1
            if count == 3:
                new_text += "-"
                count = 0
        else:
            if count != 0:
                new_text += "-"
                count = 0
            new_text += text[i]
    
    return new_text
