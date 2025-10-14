def fix_spaces(text):
    text = text.replace(" ", "_")
    i = 0
    while i < len(text):
        if i < len(text) - 2 and text[i:i+3] == "___":
            text = text[:i] + "-" + text[i+3:]
        elif i < len(text) - 1 and text[i:i+2] == "__":
            text = text[:i] + "-" + text[i+2:]
        i += 1
    return text
