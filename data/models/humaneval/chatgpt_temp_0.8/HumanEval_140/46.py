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
    # First, replace all spaces with underscores
    text = text.replace(" ", "_")

    # Then, find all occurrences of 3 or more consecutive underscores and replace them with a dash
    import re
    text = re.sub(r"_{3,}", "-", text)

    # If the string starts with a space, add an underscore to the beginning
    if text[0] == " ":
        text = "_" + text[1:]

    # If the string ends with a space, add an underscore to the end
    if text[-1] == " ":
        text = text[:-1] + "_"

    return text
