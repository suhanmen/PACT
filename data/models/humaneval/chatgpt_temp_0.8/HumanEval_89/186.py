def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[2*2:] + alphabet[:2*2]
    encrypted_string = ''
    
    for char in s:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_string += rotated_alphabet[index]
        else:
            encrypted_string += char
    
    return encrypted_string
