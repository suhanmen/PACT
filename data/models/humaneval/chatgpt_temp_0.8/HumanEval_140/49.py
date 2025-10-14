def fix_spaces(text):
    text = text.replace(" ", "_")
    if "   " in text:
        text = text.replace("   ", "-")
    elif "  " in text:
        text = text.replace("  ", "-")
    return text
