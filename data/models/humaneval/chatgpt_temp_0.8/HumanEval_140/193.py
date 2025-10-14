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
    i = 0
    output = ""
    while i < len(text):
        if text[i] == " ":
            if i < len(text) - 2 and text[i+1] == " " and text[i+2] == " ":
                output += "-"
                i += 3
                while i < len(text) and text[i] == " ":
                    i += 1
            else:
                output += "_"
                i += 1
        else:
            output += text[i]
            i += 1
    return output
