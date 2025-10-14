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
    encrypted = ''
    for c in s:
        # Check if character is a letter
        if c.isalpha():
            # Convert to lowercase and convert to ASCII code
            ascii_value = ord(c.lower())
            # Shift down by two multiplied to two places
            shifted_ascii = (ascii_value - 97 + (2**2)) % 26 + 97
            # Convert back to character and add to result string
            encrypted += chr(shifted_ascii)
        else:
            encrypted += c
    return encrypted
