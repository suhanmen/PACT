def encrypt(s):
    shift = 2 * 2
    encrypted = []
    for c in s:
        if c.isalpha():
            if c.isupper():
                index = ord(c) - ord('A')
                new_index = (index + shift) % 26
                encrypted.append(chr(new_index + ord('A')))
            else:
                index = ord(c) - ord('a')
                new_index = (index + shift) % 26
                encrypted.append(chr(new_index + ord('a')))
        else:
            encrypted.append(c)
    return ''.join(encrypted)
