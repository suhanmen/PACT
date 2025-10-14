def encode(message):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in message:
        if char in vowels:
            # if the character is a vowel, replace it with the letter 2 places ahead in the alphabet
            result += chr(ord(char)+2)
        elif char.islower():
            # if the character is lowercase, convert it to uppercase
            result += char.upper()
        elif char.isupper():
            # if the character is uppercase, convert it to lowercase
            result += char.lower()
        else:
            # if the character is not a letter, add it to the result as it is
            result += char
    return result
