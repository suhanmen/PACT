def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for letter in message:
        # Swap case of all letters
        if letter.isalpha():
            if letter.islower():
                letter = letter.upper()
            else:
                letter = letter.lower()
        # Replace all vowels with the letter 2 places ahead in the alphabet
        if letter in vowels:
            if letter == 'u':
                result += 'W'
            elif letter == 'U':
                result += 'w'
            elif letter == 'e':
                result += 'G'
            elif letter == 'E':
                result += 'g'
            elif letter == 'o':
                result += 'Q'
            elif letter == 'O':
                result += 'q'
            elif letter == 'a':
                result += 'C'
            elif letter == 'A':
                result += 'c'
            elif letter == 'i':
                result += 'K'
            elif letter == 'I':
                result += 'k'
        else
