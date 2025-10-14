def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    """
    encrypted = ''
    for char in s:
        if char.isalpha():
            shifted = chr(ord(char) + 2 * 2)
            if shifted > 'z':
                shifted = chr(ord(shifted) - 26)
            encrypted += shifted
        else:
            encrypted += char
    return encrypted
