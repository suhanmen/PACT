def encrypt(s):
    shifted_alphabet = ''
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        shifted_letter = chr((ord(letter) - 97 + 2 * 2) % 26 + 97)
        shifted_alphabet += shifted_letter
    encrypted_s = ''
    for letter in s:
        if letter.isalpha():
            encrypted_letter = shifted_alphabet[ord(letter.lower()) - 97]
            if letter.isupper():
                encrypted_s += encrypted_letter.upper()
            else:
                encrypted_s += encrypted_letter
        else:
            encrypted_s += letter
    return encrypted_s
