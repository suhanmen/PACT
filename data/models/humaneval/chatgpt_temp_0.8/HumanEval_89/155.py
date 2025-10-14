def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    encrypted = ''
    for c in s:
        if c.isalpha():
            index = alphabet.find(c.lower())
            shifted_char = shifted_alphabet[index]
            if c.isupper():
                encrypted += shifted_char.upper()
            else:
                encrypted += shifted_char
        else:
            encrypted += c
    return encrypted
