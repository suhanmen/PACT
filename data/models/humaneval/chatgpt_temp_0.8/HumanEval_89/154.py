def encrypt(s):
    # Define the alphabet and the number of positions to shift it
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 2 * 2

    # Define the encrypted string
    encrypted = ''

    # Loop over each character in the input string
    for c in s:
        # Find the index of the current character in the alphabet
        index = alphabet.find(c)

        # If the character is not in the alphabet, add it to the encrypted string as-is
        if index == -1:
            encrypted += c
        else:
            # Shift the index by the desired number of positions
            shifted_index = (index + shift) % 26

            # Add the corresponding character to the encrypted string
            encrypted += alphabet[shifted_index]

    return encrypted
