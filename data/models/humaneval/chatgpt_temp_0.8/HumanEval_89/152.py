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
    encrypted_string = ''
    for letter in s:
        # Convert the letter to its ASCII code
        letter_code = ord(letter)
        # Shift the ASCII code down by two multiplied to two places
        shifted_code = letter_code + (2 * 2)
        # If the shifted code is greater than the ASCII code for 'z', wrap it around to 'a'
        if shifted_code > ord('z'):
            shifted_code = shifted_code - 26
        # Convert the shifted code back to a letter and append it to the encrypted string
        encrypted_string += chr(shifted_code)
    return encrypted_string
