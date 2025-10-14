def encrypt(s):
    # Define a variable to store the rotated alphabet
    new_alphabet = ''
    # Loop through the lowercase letters of the alphabet
    for i in range(97, 123):
        # Compute the new index by adding 2 * 2 to the ASCII code
        new_index = (i - 97 + 2 * 2) % 26
        # Compute the new character by adding the new index to lowercase 'a'
        new_char = chr(new_index + 97)
        # Append the new character to the new alphabet
        new_alphabet += new_char
    # Define a variable to store the encrypted string
    encrypted = ''
    # Loop through the characters of the input string
    for c in s:
        # If the character is lowercase, replace it with the corresponding
        # character in the new alphabet, otherwise keep it unchanged
        if c.islower():
            encrypted += new_alphabet[ord(c) - 97]
        else:
            encrypted += c
    # Return the encrypted string
    return encrypted
