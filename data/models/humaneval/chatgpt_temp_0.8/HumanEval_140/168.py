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
    consecutive_spaces = 0
    for c in text:
        if c == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                new_text += "-"
        else:
            consecutive_spaces = 0
        new_text += c if c != " " else ("_" if consecutive_spaces <= 2 else "-")
    return new_text
