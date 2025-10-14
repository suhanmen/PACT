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
    # Convert all spaces to underscores
    text = text.replace(" ", "_")

    # Convert 3 or more consecutive underscores to dashes
    text = text.replace("__", "-")
    while "__" in text:
        text = text.replace("__", "-")

    # Convert 2 consecutive underscores to single underscores
    text = text.replace("__", "_")

    return text
