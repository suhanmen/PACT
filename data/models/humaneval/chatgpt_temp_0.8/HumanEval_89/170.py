def encrypt(s):
    # Define the original alphabet and the shifted alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[2:] + alphabet[:2]

    # Encrypt the string by mapping each character to its shifted counterpart
    encrypted = ''
    for c in s:
        if c in alphabet:
            encrypted += shifted_alphabet[alphabet.index(c)]
        else:
            encrypted += c
    return encrypted
