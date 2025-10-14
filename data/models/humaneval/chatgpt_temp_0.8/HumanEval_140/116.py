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
    fixed_text = text.replace(" ", "_")
    consecutive_spaces = 0
    for i in range(len(fixed_text)):
        if fixed_text[i] == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                fixed_text = fixed_text[:i-consecutive_spaces+1] + "-" + fixed_text[i+1:]
        else:
            consecutive_spaces = 0
    return fixed_text
