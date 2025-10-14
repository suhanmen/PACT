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

    # Create a string with all the alphabets
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Rotate the alphabet down by two multiplied to two places
    rotated_alphabet = alphabet[4:] + alphabet[:4]

    # Create a dictionary that maps each letter in the original alphabet to 
    # the corresponding letter in the rotated alphabet
    mapping = {}
    for i in range(len(alphabet)):
        mapping[alphabet[i]] = rotated_alphabet[i]

    # Use the mapping to encrypt the input string
    encrypted = ''
    for c in s:
        if c in mapping:
            encrypted += mapping[c]
        else:
            encrypted += c

    return encrypted
