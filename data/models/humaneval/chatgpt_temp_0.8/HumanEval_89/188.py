def encrypt(s):
    # Define the original and rotated alphabets
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotated_alpha = alpha[4:] + alpha[:4]

    # Create a dictionary mapping from original to rotated letters
    alpha_map = dict(zip(alpha, rotated_alpha))

    # Encrypt the string by replacing each letter with the rotated one
    encrypted = ''
    for letter in s:
        if letter.isalpha():
            encrypted += alpha_map[letter]
        else:
            encrypted += letter

    return encrypted
