python
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
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                new_char = chr((ord(i) - ord('a') + 2 * 2) % 26 + ord('a'))
            else:
                new_char = chr((ord(i) - ord('A') + 2 * 2) % 26 + ord('A'))
        else:
            new_char = i
        result += new_char
    return result
