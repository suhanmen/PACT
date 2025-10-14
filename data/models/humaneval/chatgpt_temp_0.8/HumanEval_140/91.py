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
    if len(text) < 2:
        return text.replace(" ", "_")
    else:
        fixed_text = ""
        num_consecutive_spaces = 0
        for i in range(len(text)):
            if text[i] == " ":
                num_consecutive_spaces += 1
                if num_consecutive_spaces > 2:
                    fixed_text += "-"
                else:
                    fixed_text += "_"
            else:
                num_consecutive_spaces = 0
                fixed_text += text[i]
        return fixed_text
