def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    result = ""
    for c in s:
        if c.isalpha():
            shifted_c = chr(((ord(c.lower()) - 97) + (2 ** 2)) % 26 + 97)
            result += shifted_c.upper() if c.isupper() else shifted_c
        else:
            result += c
    return result
