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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[-2:] + alphabet[:-2]  # shift alphabet down by 2
    shifted_alphabet = shifted_alphabet * 2  # multiply shifted alphabet by 2
    table = str.maketrans(alphabet, shifted_alphabet)  # create translation table
    return s.translate(table)  # use translation table to encrypt string
