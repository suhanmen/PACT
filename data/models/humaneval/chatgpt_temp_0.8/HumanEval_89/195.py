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
    encrypted = ""
    for letter in s:
        if letter.isalpha():
            shifted = ord(letter) + 2 * 2
            if letter.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted += chr(shifted)
            else:
                if shifted > ord('z'):
                    shifted -= 26
                encrypted += chr(shifted)
        else:
            encrypted += letter
    return encrypted
