def encrypt(s):
    new_s = ''
    for c in s:
        if c.isalpha():
            new_c = chr(((ord(c.lower()) - 97 + (2*2)) % 26) + 97)
            if c.isupper():
                new_s += new_c.upper()
            else:
                new_s += new_c
        else:
            new_s += c
    return new_s
