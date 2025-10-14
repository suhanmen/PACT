def encrypt(s):
    # define the alphabet as a string
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # shift the letters down by 2*2=4 places
    shifted_alphabet = alphabet[4:] + alphabet[:4]
    # create a translation table to map each character in the original alphabet to the shifted one
    trans_table = str.maketrans(alphabet, shifted_alphabet)
    # use the translation table to encrypt the input string
    return s.translate(trans_table)
