python
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
    
    # Replace any consecutive spaces with -
    replaced_text = ''
    counter = 0
    for char in text:
        if char == ' ':
            counter += 1
            if counter > 2:
                replaced_text += '-'
        else:
            counter = 0
        replaced_text += char
        
    return replaced_text
