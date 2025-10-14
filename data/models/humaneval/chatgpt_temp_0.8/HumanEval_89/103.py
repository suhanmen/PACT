def encrypt(s):
    shift = 2 * 2
    encrypted_text = ""
    for char in s:
        if char.isalpha():
            shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text
