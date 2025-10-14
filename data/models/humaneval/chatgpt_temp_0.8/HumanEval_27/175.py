def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ""
    for character in string:
        if character.islower():
            flipped_string += character.upper()
        elif character.isupper():
            flipped_string += character.lower()
        else:
            flipped_string += character
    return flipped_string
