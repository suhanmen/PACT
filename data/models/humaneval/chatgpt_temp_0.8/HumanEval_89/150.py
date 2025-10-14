def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alphabet[2:] + alphabet[:2] + alphabet.upper()[2:] + alphabet.upper()[:2]
    translation_table = s.maketrans(alphabet + alphabet.upper(), new_alphabet)
    encrypted_string = s.translate(translation_table)
    return encrypted_string
