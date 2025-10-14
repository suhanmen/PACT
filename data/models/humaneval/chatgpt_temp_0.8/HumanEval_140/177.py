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
    text = text.replace(" ", "_")  # replace spaces with underscores
    for i in range(2, len(text)):
        if text[i] == "_" and text[i - 1] == "_" and text[i - 2] == "_":
            j = i
            while j < len(text) and text[j] == "_":
                j += 1
            if j - i > 2:
                text = text[:i] + "-" + text[j:]
    return text
