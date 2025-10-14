def encrypt(s):
    shift = 2 * 2
    result = ''
    for c in s:
        if c.isalpha():
            ascii_code = ord(c)
            if c.islower():
                base = ord('a')
            else:
                base = ord('A')
            new_ascii_code = ((ascii_code - base + shift) % 26) + base
            result += chr(new_ascii_code)
        else:
            result += c
    return result
