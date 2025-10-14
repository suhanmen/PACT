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
            new_char_code = ord(char) + (2 * 2)
            if char.islower():
                if new_char_code > ord('z'):
                    new_char_code -= 26
                elif new_char_code < ord('a'):
                    new_char_code += 26
            elif char.isupper():
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                elif new_char_code < ord('A'):
                    new_char_code += 26
            result += chr(new_char_code)
        else:
            result += char
    return result
