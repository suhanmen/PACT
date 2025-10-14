def encrypt(s):
    shift = 2 * 2
    enc = ''
    for letter in s:
        if letter.isalpha():
            new_letter = chr((ord(letter.lower()) - 97 + shift) % 26 + 97)
            if letter.isupper():
                enc += new_letter.upper()
            else:
                enc += new_letter
        else:
            enc += letter
    return enc
