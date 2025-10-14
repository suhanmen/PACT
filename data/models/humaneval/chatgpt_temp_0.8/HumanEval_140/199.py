def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.strip() # removing leading and trailing spaces
    if len(text) <= 2:  # if length of text is less than or equal to 2, just replace spaces with underscores
        return text.replace(' ', '_')
    else:
        prev_char = ''
        new_text = ''
        consecutive_space_count = 0
        for char in text:
            if char == ' ':
                consecutive_space_count += 1
                if consecutive_space_count > 2:
                    new_text += '-'
                else:
                    new_text += '_'
            else:
                consecutive_space_count = 0
                new_text += char
        if new_text[0] == ' ':
            new_text = '_' + new_text[1:]
        return new_text
