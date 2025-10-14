def fix_spaces(text):
    text = text.strip()  # Remove leading and trailing spaces
    if '  ' not in text:  # No consecutive spaces
        return text.replace(' ', '_')
    else:
        text = text.replace(' ', '-')  # Replace consecutive spaces with -
        while '--' in text:
            text = text.replace('--', '-')  # Remove any double hyphens
        return '_' + text.replace(' ', '_').replace('-', '', 1)  # Replace remaining spaces with underscores
