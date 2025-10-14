def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ""
    for letter in string:
        if letter.isupper():
            flipped_string += letter.lower()
        elif letter.islower():
            flipped_string += letter.upper()
        else:
            flipped_string += letter

    return flipped_string
