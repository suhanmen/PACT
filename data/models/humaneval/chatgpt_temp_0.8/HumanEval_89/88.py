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
        # Converting the character into its ASCII code
        c = ord(i)
        
        # Subtracting 97 from the code to obtain a value between 0 and 25
        c = c - 97
        
        # Rotating the value by 2 times the square of 2, modulo 26
        c = (c + 2*2**2) % 26
        
        # Converting the rotated value back into a character
        c = chr(c + 97)
        
        # Adding the new character to the result
        result += c
    
    return result
