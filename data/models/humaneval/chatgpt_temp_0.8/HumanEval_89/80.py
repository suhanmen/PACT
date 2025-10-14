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

    # Rotate the alphabet down by two multiplied to two places
    rotated_alphabet = alphabet[2*2:] + alphabet[:2*2]

    # Create a translation table to map each character in s to its corresponding encrypted character
    translation_table = str.maketrans(alphabet, rotated_alphabet)

    # Use the translation table to encrypt the string s
    encrypted_s = s.translate(translation_table)

    return encrypted_s
