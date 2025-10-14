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
    text = text.replace(" ", "_")  # replace all single spaces with underscores
    consecutive_spaces = False
    result = ""
    for i in range(len(text)):
        if text[i] == " ":
            if not consecutive_spaces:
                # start of consecutive spaces
                result += "_"
                consecutive_spaces = True
            else:
                # already in consecutive spaces
                result += "-"
        else:
            # not in consecutive spaces anymore
            result += text[i]
            consecutive_spaces = False
    return result
