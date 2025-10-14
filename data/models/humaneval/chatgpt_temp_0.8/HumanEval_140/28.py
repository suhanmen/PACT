def fix_spaces(text):
    new_text = text.replace(" ", "_")
    consecutive_spaces = 0
    for i in range(len(new_text)):
        if new_text[i] == " ":
            consecutive_spaces += 1
            if consecutive_spaces > 2:
                new_text = new_text[:i-consecutive_spaces+1] + "-" + new_text[i+1:]
        else:
            consecutive_spaces = 0
    if new_text.startswith(" "):
        new_text = "_" + new_text[1:]
    return new_text
