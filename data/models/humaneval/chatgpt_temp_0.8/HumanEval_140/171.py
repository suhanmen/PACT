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
    fixed_text = text.replace(' ', '_') # replace single spaces with underscores
    if '   ' in fixed_text: # if more than 2 consecutive spaces are present
        fixed_text = fixed_text.replace('   ', '-') # replace all consecutive spaces with -
        fixed_text = fixed_text.replace('__', '_-') # add - between underscores to maintain proper formatting
    return fixed_text
