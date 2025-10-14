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

    # Rotate the alphabet
    rotated_alphabet = alphabet[2*2:] + alphabet[:2*2]

    # Encrypt the string
    encrypted_string = ''
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_string += rotated_alphabet[index]
        else:
            encrypted_string += char

    return encrypted_string
