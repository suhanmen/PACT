def encode(message):
    vowels = "aeiouAEIOU"
    encoded = ""
    for char in message:
        if char in vowels:
            # Replace the vowel with the letter 2 places ahead in the alphabet
            encoded += chr(ord(char) + 2)
        elif char.isalpha():
            # Swap the case of the letter
            if char.islower():
                encoded += char.upper()
            else:
                encoded += char.lower()
        else:
            encoded += char
    return encoded
