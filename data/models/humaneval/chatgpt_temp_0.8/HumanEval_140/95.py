def fix_spaces(text):
    # Replace all spaces with underscores
    text = text.replace(" ", "_")

    # Replace more than 2 consecutive spaces with a hyphen
    while "___" in text:
        text = text.replace("___", "-")
    while "__" in text:
        text = text.replace("__", "_")

    # If the string starts with spaces, add an underscore at the beginning
    if text.startswith(" "):
        text = "_" + text[1:]

    # If the string ends with spaces, add an underscore at the end
    if text.endswith(" "):
        text = text[:-1] + "_"

    return text
