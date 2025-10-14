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
    new_str = ""
    for char in s:
        if char.isalpha():
            new_char = chr(((ord(char.lower()) - 97 + 2 * 2) % 26) + 97)
            if char.isupper():
                new_char = new_char.upper()
            new_str += new_char
        else:
            new_str += char
    return new_str
