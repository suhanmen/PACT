def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores,
    and if a string has more than 2 consecutive spaces,
    then replace all consecutive spaces with -
    """
    text = text.replace(" ", "_")  # replace spaces with underscores
    space_count = 0  # variable to count consecutive spaces
    new_text = ""  # variable to store modified string
    for char in text:
        if char == " ":
            space_count += 1
        else:
            if space_count > 2:
                new_text += "-"
            elif space_count > 0:
                new_text += "_"
            space_count = 0
            new_text += char
    if space_count > 2:
        new_text += "-"
    elif space_count > 0:
        new_text += "_"
    return new_text
