python
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
    new_text = ""
    count_spaces = 0
    
    for i in range(len(text)):
        if text[i] == " ":
            count_spaces += 1
            if count_spaces > 2:
                new_text += "-"
        else:
            if count_spaces > 2:
                new_text += "-"
            new_text += "_" if count_spaces > 0 else text[i]
            count_spaces = 0
    
    if count_spaces > 2:
        new_text += "-"
            
    return new_text
