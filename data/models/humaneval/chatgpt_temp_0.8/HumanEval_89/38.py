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
    for c in s:
        # Convert the character to its ASCII code
        ascii_code = ord(c)
        
        # Check if the character is lowercase 
        if c.islower():
            # Subtract 97 to get the index of the character in the alphabet
            index = ascii_code - 97
            
            # Shift the index down by 2 x 2 places
            new_index = (index + (2 * 2)) % 26
            
            # Convert the new index back to an ASCII code and then to a character
            new_char = chr(new_index + 97)
            
            # Add the new character to the result string
            result += new_char
        else:
            # If the character is not lowercase, add it to the result string as-is
            result += c
    
    return result
