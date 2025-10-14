def encrypt(s):
    shift = 2 * 2
    result = ""
    for char in s:
        if char.isalpha():
            ascii_code = ord(char)
            shifted_ascii_code = ascii_code + shift
            if char.isupper():
                while shifted_ascii_code > ord('Z'):
                    shifted_ascii_code -= 26
            else:
                while shifted_ascii_code > ord('z'):
                    shifted_ascii_code -= 26
            result += chr(shifted_ascii_code)
        else:
            result += char
    return result
