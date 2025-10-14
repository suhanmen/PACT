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
    for i in s:
        if i.isalpha():
            # Get the ASCII value of the character
            ascii_val = ord(i)

            # Shift the ASCII value down by 2 and multiply by 2
            shifted_val = ((ascii_val - 97) + 24) % 26 + 97

            # Convert the shifted ASCII value back to a character and append to result
            result += chr(shifted_val)
        else:
            result += i
    return result
