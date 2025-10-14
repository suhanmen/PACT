def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_str = ""
    for char in string:
        if char.isupper():
            flipped_str += char.lower()
        elif char.islower():
            flipped_str += char.upper()
        else:
            flipped_str += char
    return flipped_str
