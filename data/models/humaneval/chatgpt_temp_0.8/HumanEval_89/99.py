def encrypt(s):
    shift = 2 * 2  # calculate the shift value
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]  # shift the alphabet
    table = str.maketrans(alphabet, shifted_alphabet)  # create a translation table
    return s.translate(table)  # use the translation table to encrypt the string
