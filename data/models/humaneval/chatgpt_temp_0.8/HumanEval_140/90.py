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
    text = text.replace(" ", "_")
    
    # Replace consecutive spaces with -
    i = 0
    while i < len(text):
        if text[i] == " ":
            # Find the end of the consecutive spaces
            j = i + 1
            while j < len(text) and text[j] == " ":
                j += 1
            
            # If there were more than 2 consecutive spaces, replace them with -
            if j - i > 2:
                text = text[:i] + "-" + text[j:]
            
            # Move the index to the end of the consecutive spaces
            i = j - 1
        
        # Move to the next character
        i += 1
    
    return text
