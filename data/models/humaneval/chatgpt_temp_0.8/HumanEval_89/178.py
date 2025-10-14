def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_code = (ascii_code - 97 + 2 * 2) % 26 + 97
            result += chr(shifted_code)
        else:
            result += char
    return result
