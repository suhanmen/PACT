def encrypt(s):
    shift = (2 * 2) % 26
    res = ""
    for i in s:
        if i.isalpha():
            res += chr((ord(i) - 97 + shift) % 26 + 97)
        else:
            res += i
    return res
