def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped = ""
    for char in string:
        if char.isupper():
            flipped += char.lower()
        else:
            flipped += char.upper()
    return flipped
