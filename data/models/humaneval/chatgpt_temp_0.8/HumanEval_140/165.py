def fix_spaces(text):
    text = text.replace(" ", "_")     # replace all spaces with underscores
    while "  " in text:               # while there are consecutive spaces
        text = text.replace("  ", " -")  # replace 2 spaces with - and 1 space
    if text.startswith(" "):          # if string starts with a space
        text = "_" + text[1:]         # replace the first space with an underscore
    return text
