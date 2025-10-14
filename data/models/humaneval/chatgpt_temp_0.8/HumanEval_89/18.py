def encrypt(s):
    result = ''
    for char in s:
        if char.isalpha():
            shifted = ord(char) + 2 * 2
            if char.islower():
                result += chr((shifted - 97) % 26 + 97)
            else:
                result += chr((shifted - 65) % 26 + 65)
        else:
            result += char
    return result
