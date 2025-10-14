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
    text = text.replace(" ", "_")  # Replace all spaces with underscores
    count = 0
    new_text = ""
    for char in text:
        if char == " ":  # Count consecutive spaces
            count += 1
        else:
            if count > 2:  # Replace consecutive spaces with -
                new_text += "-"
            new_text += " " * count  # Add counted spaces to new_text
            count = 0
            new_text += char
    if count > 2:  # Replace consecutive spaces at end with -
        new_text += "-"
    new_text += " " * count  # Add counted spaces at end to new_text
    return new_text.strip()  # Remove any leading/trailing spaces
