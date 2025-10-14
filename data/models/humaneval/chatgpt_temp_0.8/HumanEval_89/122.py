def encrypt(s):
    shifted_alphabet = ''
    for i in range(26):
        shifted_alphabet += chr((i + (2 * 2)) % 26 + ord('a'))
    
    encrypted_string = ''
    for letter in s:
        if letter.isalpha():
            if letter.isupper():
                encrypted_string += shifted_alphabet[ord(letter.lower()) - ord('a')].upper()
            else:
                encrypted_string += shifted_alphabet[ord(letter) - ord('a')]
        else:
            encrypted_string += letter
                
    return encrypted_string
