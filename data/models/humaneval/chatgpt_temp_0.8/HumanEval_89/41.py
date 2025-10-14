def encrypt(s):
    """
    Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Create a string with the alphabet rotated
    alphabet = 'cdefghijklmnopqrstuvwxyzab'
    
    # Create an empty string to store the encrypted string
    encrypted_s = ''
    
    # Loop through each character in the input string
    for char in s:
        # If the character is a space, add it to the encrypted string
        if char == ' ':
            encrypted_s += ' '
        # If the character is a letter, find its index in the original alphabet
        # and add the rotated letter to the encrypted string
        else:
            index = ord(char) - ord('a')
