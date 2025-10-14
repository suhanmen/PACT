def encode(message):
    result = ""
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                result += letter.lower()
            else:
                result += letter.upper()
            if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
                result = result[:-1] + chr(ord(letter)+2)
        else:
            result += letter
    return result
