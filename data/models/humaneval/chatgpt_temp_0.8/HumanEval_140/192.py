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
    while i < len(text):
        if text[i:i+3] == "___": # check for 3 consecutive underscores
            j = i+3
            while j < len(text) and text[j] == "_": # find the end of the consecutive underscores
                j += 1
            text = text[:i] + "_" + text[j:] # replace the consecutive underscores with a single underscore
        elif text[i:i+2] == "__": # check for 2 consecutive underscores
            text = text[:i] + "-" + text[i+2:] # replace the consecutive underscores with a hyphen
            i += 1
        else:
          
