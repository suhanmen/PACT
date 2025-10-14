def encrypt(s):
    encrypted = ''
    for i in s:
        if i.isalpha():
            new_ascii = ord(i) + (2*2)
            if new_ascii > ord('z'):
                new_ascii -= 26
            encrypted += chr(new_ascii)
        else:
            encrypted += i
    return encrypted
