def encrypt(s):
    shift = 2 * 2
    encrypted = ''
    for char in s:
        if char.isalpha():
            char_code = ord(char) + shift
            if char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            elif char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            encrypted += chr(char_code)
        else:
            encrypted += char
    return encrypted
