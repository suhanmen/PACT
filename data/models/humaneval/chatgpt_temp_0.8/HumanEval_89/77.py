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
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    
    for letter in s:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + (2 * 2)) % 26
            new_string += alphabet[new_index]
        else:
            new_string += letter
    
    return new_string
