def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[2*2:] + alphabet[:2*2]
    return s.translate(str.maketrans(alphabet, shifted_alphabet))
