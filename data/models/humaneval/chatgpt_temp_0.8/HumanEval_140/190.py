def fix_spaces(text):
    text = text.replace(" ", "_")
    count = 0
    new_text = ""
    for i in range(len(text)):
        if text[i] == "_":
            count = 0
            new_text += "_"
        else:
            count += 1
            if count > 2:
                new_text = new_text[:-2] + "-"
                count = 1
            else:
                new_text += text[i]
    return new_text
