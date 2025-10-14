def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted_s = ''
    for c in s:
        if c.isalpha():
            shift = (ord(c.lower()) - ord('a') + 2) ** 2
            if c.isupper():
                encrypted_s += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_s += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_s += c
    return encrypted_s
