def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for letter in s:
        if letter in alphabet:
            index = (alphabet.index(letter) + shift) % len(alphabet)
            encrypted += alphabet[index]
        else:
            encrypted += letter
    
    return encrypted
