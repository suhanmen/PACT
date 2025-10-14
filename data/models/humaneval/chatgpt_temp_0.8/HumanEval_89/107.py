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
    output = ''
    for char in s:
        if char.isalpha():
            # Convert the letter to its ASCII code, subtract 97 for 'a' as the starting point
            # Rotate the value by the shift amount, mod by 26 to wrap around
            # Add 97 back to get back to ASCII values for letters
            shifted = chr(((ord(char) - 97) + (2 * 2)) % 26 + 97)
            output += shifted
        else:
            output += char
    return output
