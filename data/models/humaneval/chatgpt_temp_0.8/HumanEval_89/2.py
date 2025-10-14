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
    for c in s:
        if c.isalpha():
            num = ord(c)
            num += (2*2)
            if c.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif c.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            result += chr(num)
        else:
            result += c
    return result
