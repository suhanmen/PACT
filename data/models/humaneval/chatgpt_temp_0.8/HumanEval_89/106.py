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
    result = ''
    for char in s:
        if char.isalpha():
            ascii_num = ord(char) + (2 * 2)
            if char.isupper():
                if ascii_num > ord('Z'):
                    ascii_num = ord('A') + (ascii_num - ord('Z')) - 1
            else:
                if ascii_num > ord('z'):
                    ascii_num = ord('a') + (ascii_num - ord('z')) - 1
            result += chr(ascii_num)
        else:
            result += char
    return result
