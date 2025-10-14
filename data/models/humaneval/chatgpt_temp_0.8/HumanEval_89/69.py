def encrypt(s):
    # Define the alphabet and the number of places to shift down
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2
    
    # Create a dictionary to map each letter to its shifted counterpart
    shifted_alphabet = {}
    for i in range(len(alphabet)):
        shifted_index = (i + shift) % len(alphabet)
        shifted_alphabet[alphabet[i]] = alphabet[shifted_index]
    
    # Encrypt the string by replacing each letter with its shifted counterpart
    result = ''
    for letter in s:
        if letter in shifted_alphabet:
            result += shifted_alphabet[letter]
        else:
            result += letter
    
    return result
