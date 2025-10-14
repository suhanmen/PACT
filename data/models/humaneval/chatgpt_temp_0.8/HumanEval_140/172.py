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
    # Replace all spaces with underscores
    text = text.replace(' ', '_')
    
    # Replace consecutive spaces with -
    count = 0
    new_text = ''
    for c in text:
        if c == ' ':
            count += 1
            if count > 2:
                new_text += '-'
            else:
                new_text += ' '
        else:
            count = 0
            new_text += c
            
    # Replace any remaining spaces with underscores
    new_text = new_text.replace(' ', '_')
    
    return new_text
