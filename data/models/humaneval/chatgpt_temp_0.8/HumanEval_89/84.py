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
        if letter.isalpha():
            # Shift the letter down by two multiplied to two places
            code = ord(letter) + 2 * 2
            # If the code goes beyond the letter 'z', wrap it back to 'a'
            if letter.islower():
                if code > ord('z'):
                    code = code - 26
            else:
                if code > ord('Z'):
                    code = code - 26
            result += chr(code)
        else:
            # If the character is not a letter, just add it to the result
            result += letter
    return result
