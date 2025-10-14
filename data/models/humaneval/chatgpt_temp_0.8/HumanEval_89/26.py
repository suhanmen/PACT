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
    for letter in s:
        # Convert to ASCII code
        ascii_code = ord(letter)
        # Add the shift
        shifted_code = ascii_code + (2 * 2)
        # If the shifted code is greater than 'z', wrap around to 'a'
        if shifted_code > ord('z'):
            shifted_code = shifted_code - 26
        # Convert back to a letter and add to the result string
        result += chr(shifted_code)
    return result
