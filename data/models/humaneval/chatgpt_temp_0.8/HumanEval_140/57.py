def fix_spaces(text):
    text = text.strip() # Remove leading and trailing spaces
    new_text = ""
    space_count = 0
    
    for char in text:
        if char == " ":
            space_count += 1
            if space_count > 2:
                new_text = new_text[:-1] + "-" # Replace consecutive spaces with -
        else:
            space_count = 0
        new_text += char.replace(" ", "_")
    
    return new_text
