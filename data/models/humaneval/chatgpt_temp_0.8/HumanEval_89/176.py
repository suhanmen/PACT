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

    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Define the shifted alphabet
    shifted_alphabet = alphabet[2 * 2:] + alphabet[:2 * 2]

    # Create a translation table using the maketrans function
    translation_table = str.maketrans(alphabet, shifted_alphabet)

    # Return the encrypted string using the translate method
    return s.translate(translation_table)
