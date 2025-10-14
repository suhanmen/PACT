def encode(message):
    vowels = "aeiouAEIOU"
    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            # swap case of letter
            if letter.isupper():
                letter = letter.lower()
            else:
                letter = letter.upper()
            # replace vowel with letter 2 places ahead
            if letter in vowels:
                letter = chr(ord(letter) + 2)
                if letter == "{":
                    letter = "A"
                elif letter == "|":
                    letter = "E"
                elif letter == "}":
                    letter = "I"
                elif letter == "~":
                    letter = "O"
                elif letter == "#":
                    letter = "U"
        encoded_message += letter
    return encoded_message
