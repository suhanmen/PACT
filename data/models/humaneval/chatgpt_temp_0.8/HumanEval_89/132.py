def encrypt(s):
    shifted_alphabet = 'cdefghijklmnopqrstuvwxyzab'
    encrypted = ''
    for char in s:
        if char.isalpha():
            shifted_char = shifted_alphabet[ord(char.lower())-97]
            encrypted += shifted_char if char.islower() else shifted_char.upper()
        else:
            encrypted += char
    return encrypted
