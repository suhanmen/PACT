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
    text = text.replace(" ", "_")  # replace all spaces with underscores
    while "--" in text:
        text = text.replace("--", "-")  # replace any double hyphens with a single hyphen
    if "___" in text:
        text = text.replace("___", "--")  # replace any triple underscores with double hyphens
    elif "__" in text:
        text = text.replace("__", "-")  # replace any double underscores with a single hyphen
    return text
