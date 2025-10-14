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
    for char in s:
        # Convert the character to its ASCII code
        ascii_code = ord(char)
        # Shift the ASCII code down by 2 multiplied by 2 places
        shifted_ascii_code = ascii_code + (2 * 2)
        # Convert the shifted ASCII code back to a character
        shifted_char = chr(shifted_ascii_code)
        # Append the shifted character to the encrypted string
        encrypted += shifted_char
    return encrypted
