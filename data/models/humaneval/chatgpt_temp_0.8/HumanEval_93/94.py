def encode(message):
    new_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                new_char = char.lower()
            else:
                new_char = char.upper()
            if new_char in "aeiouAEIOU":
                new_char = chr(ord(new_char) + 2)
                if new_char in "aeiou":
                    new_char = new_char.upper()
            new_message += new_char
        else:
            new_message += char
    return new_message
