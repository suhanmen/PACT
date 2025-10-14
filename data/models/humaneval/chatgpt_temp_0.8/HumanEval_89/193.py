def encrypt(s):
    rotated_alphabet = ''.join([chr(((ord(c)-97) + (2*2)) % 26 + 97) for c in 'abcdefghijklmnopqrstuvwxyz'])
    encrypted_string = ''
    for c in s:
        if c.isalpha():
            encrypted_string += rotated_alphabet[ord(c.lower()) - 97]
        else:
            encrypted_string += c
    return encrypted_string
