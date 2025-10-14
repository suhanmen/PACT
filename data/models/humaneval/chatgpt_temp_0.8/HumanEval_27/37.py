def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_case = ""
    for char in string:
        if char.islower():
            flipped_case += char.upper()
        elif char.isupper():
            flipped_case += char.lower()
        else:
            flipped_case += char
    return flipped_case
