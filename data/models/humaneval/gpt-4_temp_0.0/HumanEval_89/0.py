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
    encrypted = ''
    for char in s:
        if char.isalpha():
            shift = 2 * 2
            char_code = ord(char) + shift
            if char.islower():
                encrypted += chr(char_code) if char_code <= ord('z') else chr(ord('a') + char_code - ord('z') - 1)
            else:
                encrypted += chr(char_code) if char_code <= ord('Z') else chr(ord('A') + char_code - ord('Z') - 1)
        else:
            encrypted += char
    return encrypted