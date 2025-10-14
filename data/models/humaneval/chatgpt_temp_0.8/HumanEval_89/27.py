def encrypt(s):
    shift = 2 * 2
    encrypted = ""
    for char in s:
        if char.isalpha():
            ascii_value = ord(char) + shift
            if char.islower():
                if ascii_value > ord('z'):
                    ascii_value -= 26
                elif ascii_value < ord('a'):
                    ascii_value += 26
            elif char.isupper():
                if ascii_value > ord('Z'):
                    ascii_value -= 26
                elif ascii_value < ord('A'):
                    ascii_value += 26
            encrypted += chr(ascii_value)
        else:
            encrypted += char
    return encrypted
