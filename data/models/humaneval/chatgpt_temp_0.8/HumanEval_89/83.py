def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = alphabet[2*2:] + alphabet[:2*2] # rotate alphabet by 2*2 positions
    mapping = str.maketrans(alphabet, rotated) # create a translation table
    return s.translate(mapping) # translate the input string using the table
