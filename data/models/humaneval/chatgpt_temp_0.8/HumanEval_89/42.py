python
def encrypt(s):
    shift = 2 * 2
    result = ''
    for char in s:
        if char.isalpha():
            ascii_val = ord(char) + shift
            if char.isupper():
                if ascii_val > ord('Z'):
                    ascii_val -= 26
                elif ascii_val < ord('A'):
                    ascii_val += 26
            elif char.islower():
                if ascii_val > ord('z'):
                    ascii_val -= 26
                elif ascii_val < ord('a'):
                    ascii_val += 26
            result += chr(ascii_val)
        else:
            result += char
    return result
