def fix_spaces(text):
    text = text.replace(" ", "_")
    i = 0
    while i < len(text)-1:
        if text[i] == " " and text[i+1] == " ":
            j = i+2
            while j < len(text) and text[j] == " ":
                j += 1
            text = text[:i] + "-" + text[j:]
        i += 1
    if text[0] == " ":
        text = "_" + text[1:]
    return text
