def fix_spaces(text):
    # Replace all spaces with underscores
    text = text.replace(" ", "_")

    # Replace consecutive spaces with a hyphen
    while "  " in text:
        text = text.replace("  ", " -")

    # Replace all remaining spaces with underscores
    text = text.replace(" ", "_")

    return text
