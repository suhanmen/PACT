def encrypt(s):
    shift = 2 * 2 # shift alphabet down by 2 multiplied to 2 places
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char in alphabet:
            index = (alphabet.index(char) + shift) % 26 # get new index of letter after shift
            encrypted += alphabet[index]
        else:
            encrypted += char
    return encrypted
