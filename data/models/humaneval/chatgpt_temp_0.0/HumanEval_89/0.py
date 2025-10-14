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
    result = ""
    for char in s:
        if char.isalpha():
            shifted = ord(char) + (2 * 2)
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                result += chr(shifted)
            else:
                if shifted > ord('z'):
                    shifted -= 26
                result += chr(shifted)
        else:
            result += char
    return result