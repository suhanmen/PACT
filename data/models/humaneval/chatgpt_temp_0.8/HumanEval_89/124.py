def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_string = ''
    for char in s:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % 26
            encrypted_string += alphabet[index]
        else:
            encrypted_string += char
    return encrypted_string
