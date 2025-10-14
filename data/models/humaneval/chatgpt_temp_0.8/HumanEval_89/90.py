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
    shift_amount = 2 * 2
    shifted_alphabet = alphabet[shift_amount:] + alphabet[:shift_amount]
    encrypted_str = ''
    for char in s:
        if char in shifted_alphabet:
            index = shifted_alphabet.index(char)
            encrypted_str += alphabet[index]
        else:
            encrypted_str += char
    return encrypted_str
