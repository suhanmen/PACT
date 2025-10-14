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
    encrypted = ''
    for char in s:
        if char.isalpha():
            # Get the ASCII code of the character and subtract 97 or 65
            # depending on whether it's lowercase or uppercase
            code = ord(char.lower()) - 97
            # Rotate the code down by 2 multiplied to 2 places
            new_code = (code + 2 ** 2) % 26
            # Convert the new code back to a character and append it to the encrypted string
            encrypted += chr(new_code + 97)
        else:
            # If the character is not alphabetic, simply append it as is
            encrypted += char
    return encrypted
