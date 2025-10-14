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
    encrypted_str = ''
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char) + (2 ** 2)) % 123)
            if shifted_char.isalpha():
                encrypted_str += shifted_char
            else:
                encrypted_str += chr(ord('a') + (ord(shifted_char) % ord('a')))
        else:
            encrypted_str += char
    return encrypted_str
