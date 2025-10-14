def encrypt(s):
    shift = 2*2 # shift amount
    alphabet = 'abcdefghijklmnopqrstuvwxyz' # lowercase alphabet
    encrypted = ''
    for char in s:
        if char.lower() in alphabet:
            index = (alphabet.index(char.lower()) + shift) % 26 # wrap around if necessary
            if char.isupper():
                encrypted += alphabet[index].upper()
            else:
                encrypted += alphabet[index]
        else:
            encrypted += char
    return encrypted
