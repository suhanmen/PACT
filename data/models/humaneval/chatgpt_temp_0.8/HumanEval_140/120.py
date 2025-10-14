def fix_spaces(text):
    text = text.strip() # remove any leading or trailing spaces
    text = text.replace(" ", "_") # replace all spaces with underscores
    if "   " in text: # if there are more than 2 consecutive spaces
        text = text.replace("   ", "-") # replace all consecutive spaces with -
    elif "  " in text: # if there are exactly 2 consecutive spaces
        text = text.replace("  ", "-") # replace them with -
    return text
