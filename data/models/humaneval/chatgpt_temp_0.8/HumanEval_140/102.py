def fix_spaces(text):
    text = text.replace(' ', '_')
    space_count = 0
    new_text = ""
    for char in text:
        if char == ' ':
            space_count += 1
        else:
            if space_count > 2:
                new_text = new_text[:-space_count] + '-' * space_count
            else:
                new_text += ' ' * space_count
            space_count = 0
            new_text += char
    if space_count > 2:
        new_text = new_text[:-space_count] + '-' * space_count
    else:
        new_text += ' ' * space_count
    return new_text.lstrip()
