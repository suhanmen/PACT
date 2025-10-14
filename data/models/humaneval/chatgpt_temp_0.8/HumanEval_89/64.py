def encrypt(s):
    shift = 2 * 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_str = ''
    for char in s:
        if char in alphabet:
            idx = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_str += alphabet[idx]
        else:
            encrypted_str += char
    return encrypted_str
