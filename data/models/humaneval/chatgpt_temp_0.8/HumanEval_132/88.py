def is_nested(string):
    # Create an empty list to store opened brackets
    opened_brackets = []
    
    # Iterate through the string, checking each character
    for char in string:
        # If the character is an opening bracket, add it to the list of opened brackets
        if char == "[":
            opened_brackets.append(char)
        # If the character is a closing bracket and there is at least one opened bracket, remove the last opened bracket
        elif char == "]" and len(opened_brackets) > 0:
            opened_brackets.pop()
    
    # If there are any opened brackets left, at least one bracket is nested, so return True
    if len(opened_brackets) > 0:
        return True
    # Otherwise, no brackets are nested, so return False
    else:
        return False
