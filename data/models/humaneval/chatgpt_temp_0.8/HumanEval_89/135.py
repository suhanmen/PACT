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
    result = ''
    for letter in s:
        if letter.isalpha():
            new_ascii = ord(letter) + 2 * 2
            if letter.isupper():
                if new_ascii > ord('Z'):
                    new_ascii -= 26
            else:
                if new_ascii > ord('z'):
                    new_ascii -= 26
            result += chr(new_ascii)
        else:
            result += letter
    return result
