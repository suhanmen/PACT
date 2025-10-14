def fix_spaces(text):
    text = text.strip()  # remove any leading or trailing spaces
    if "  " in text:
        text = text.replace("  ", "-")
    text = text.replace(" ", "_")
    return text
