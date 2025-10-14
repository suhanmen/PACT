def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    """
    encrypted_str = ""
    for i in s:
        if i.isalpha():
            shifted_letter = chr((ord(i) - 97 + (2 * 2)) % 26 + 97)
            encrypted_str += shifted_letter
        else:
            encrypted_str += i
    return encrypted_str
