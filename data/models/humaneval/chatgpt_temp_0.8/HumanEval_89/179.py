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
    result = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                result += chr((ord(c) + 2 * 2 - 65) % 26 + 65)
            else:
                result += chr((ord(c) + 2 * 2 - 97) % 26 + 97)
        else:
            result += c
    return result
