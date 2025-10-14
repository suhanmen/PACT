def encrypt(s):
    shift = 2 * 2
    result = ''
    for char in s:
        if char.isalpha():
            val = ord(char) + shift
            if char.isupper():
                if val > ord('Z'):
                    val -= 26
                elif val < ord('A'):
                    val += 26
            else:
                if val > ord('z'):
                    val -= 26
                elif val < ord('a'):
                    val += 26
            result += chr(val)
        else:
            result += char
    return result
