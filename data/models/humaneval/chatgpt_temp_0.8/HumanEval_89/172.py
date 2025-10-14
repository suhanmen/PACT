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
    encrypted_str = ""
    for letter in s:
        # use ord() to convert the letter to its corresponding ASCII code
        # subtract 97 to get the letter's index in the alphabet (assuming lowercase)
        # add (2*2) to the index to shift it down
        # mod 26 to wrap around to the beginning of the alphabet if necessary
        # add 97 back to get the ASCII code of the encrypted letter
        encrypted_letter = chr((ord(letter) - 97 + (2*2)) % 26 + 97)
        encrypted_str += encrypted_letter
    return encrypted_str
