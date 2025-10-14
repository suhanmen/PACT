def encode(message):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ''
    
    for letter in message:
        if letter.lower() in vowels:
            encoded_letter = chr(ord(letter.lower()) + 2)
        else:
            encoded_letter = letter.swapcase()
        result += encoded_letter
        
    return result
