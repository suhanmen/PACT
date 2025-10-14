def fix_spaces(text):
    text = text.strip()  # remove any leading/trailing spaces
    new_text = ""
    consecutive_spaces = 0
    for char in text:
        if char == " ":
            consecutive_spaces += 1
            if consecutive_spaces == 3:
                new_text += "-"
                consecutive_spaces = 0
        else:
            if consecutive_spaces > 0:
                new_text += "_"
                consecutive_spaces = 0
            new_text += char
    return new_text
