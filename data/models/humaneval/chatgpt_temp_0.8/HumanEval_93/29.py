def encode(message):
    encoded = ''
    vowels = 'aeiouAEIOU'
    for ch in message:
        if ch.isalpha():
            if ch in vowels:
                encoded += chr(ord(ch) + 2)
            else:
                encoded += ch.swapcase()
        else:
            encoded += ch
    return encoded
