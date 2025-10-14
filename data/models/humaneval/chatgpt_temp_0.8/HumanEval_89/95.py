python
def encrypt(s):
    result = []
    for c in s:
        if c.isalpha():
            shift = (ord(c.lower()) - ord('a') + 2) * 2
            new_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_c)
        else:
            result.append(c)
    return ''.join(result)
