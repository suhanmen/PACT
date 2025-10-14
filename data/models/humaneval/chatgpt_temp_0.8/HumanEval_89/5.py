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
    shifted_letters = []
    for letter in s:
        new_ord = ord(letter) + (2 * 2)
        if new_ord > ord('z'):
            new_ord -= 26
        shifted_letters.append(chr(new_ord))
    return ''.join(shifted_letters)
