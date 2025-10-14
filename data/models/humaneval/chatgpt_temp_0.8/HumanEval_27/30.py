def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ""
    
    for char in string:
        if char.isupper():
            flipped_string += char.lower()
        elif char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char
    
    return flipped_string
