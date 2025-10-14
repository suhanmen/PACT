def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with -
    """
    # Replace all spaces with underscore first
    text = text.replace(" ", "_")
    
    # Replace consecutive spaces with -
    count = 0
    for i in range(len(text)):
        if text[i] == " ":
            count += 1
            if count > 2:
                text = text[:i-count+1] + "-" + text[i+1:]
        else:
            count = 0
    
    return text
