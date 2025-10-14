def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted = alphabet[2*2:] + alphabet[:2*2]
    return s.translate(s.maketrans(alphabet, shifted))
