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

    shift = 2 * 2  # Shift down by 4 letters
    result = ""
    for c in s:
        if c.isalpha():
            # Rotate the letter by the shift amount
            new_char_code = ord(c) + shift
            if c.islower():
                # Handle lowercase letters
                if new_char_code > ord("z"):
                    new_char_code -= 26
                elif new_char_code < ord("a"):
                    new_char_code += 26
            else:
                # Handle uppercase letters
                if new_char_code > ord("Z"):
                    new_char_code -= 26
                elif new_char_code < ord("A"):
                    new_char_code += 26
            
            # Add the rotated letter to the result
            result += chr(new_char_code)
        else:
            # If the character is not a letter, just add it to the result
            result += c
    return result
