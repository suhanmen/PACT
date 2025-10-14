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
    underscore_text = text.replace(' ', '_')
    hyphen_text = underscore_text.replace('___', '-')
    while '__' in hyphen_text:
        hyphen_text = hyphen_text.replace('__', '_')
    return hyphen_text
