def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result
