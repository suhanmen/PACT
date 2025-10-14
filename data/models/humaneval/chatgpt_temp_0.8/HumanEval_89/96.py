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
    encrypted = ""
    for c in s:
        if c.isalpha():
            shift = (ord(c.lower()) - 97 + 2 * 2) % 26
            encrypted += chr(shift + 97) if c.islower() else chr(shift + 65)
        else:
            encrypted += c
    return encrypted
