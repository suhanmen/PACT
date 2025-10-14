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
    encrypted_string = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                encrypted_string += chr((ord(i) + (2 * 2)) % 123 % 97 + 97)
            else:
                encrypted_string += chr((ord(i) + (2 * 2)) % 91 % 65 + 65)
        else:
            encrypted_string += i
    return encrypted_string
