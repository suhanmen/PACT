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
    shift = 2 * 2
    encrypted = ''
    for letter in s:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift) % 26
            encrypted += alphabet[index]
        else:
            encrypted += letter
    return encrypted
