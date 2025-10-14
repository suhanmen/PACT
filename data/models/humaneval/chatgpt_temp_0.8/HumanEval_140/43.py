def fix_spaces(text):
    new_text = text.replace(" ", "_")  # Replace single spaces with underscores
    new_text = re.sub(r"\s{2,}", "-", new_text)  # Replace consecutive spaces with hyphens
    if new_text.startswith(" "):  # If the string starts with a space, replace it with an underscore
        new_text = "_" + new_text[1:]
    return new_text
