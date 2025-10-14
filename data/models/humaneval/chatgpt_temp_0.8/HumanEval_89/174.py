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
        # Rotate the character down by two multiplied by two places
        new_char = chr(ord(char) + 4)
        # If the new character exceeds 'z', wrap around to 'a'
        if new_char > 'z':
            new_char = chr(ord(new_char) - 26)
        result += new_char
        
    return result
