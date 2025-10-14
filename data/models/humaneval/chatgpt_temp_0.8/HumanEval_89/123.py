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
    shifted_alphabet = alphabet[2:] + alphabet[:2] # shift letters down by 2 multiplied to 2 places
    mapping = str.maketrans(alphabet, shifted_alphabet) # create a mapping between the original alphabet and the shifted alphabet
    return s.translate(mapping) # apply the mapping to the input string to obtain the encrypted string
