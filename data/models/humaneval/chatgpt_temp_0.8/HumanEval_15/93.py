def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 up to n inclusive. """
    result = ""
    for i in range(n+1):
        result += str(i) + " "
    return result.strip()
