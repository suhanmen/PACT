def encrypt(s):
    encrypted = ""
    for char in s:
        # Check if character is an uppercase letter
        if char.isupper():
            # Encrypt uppercase letters
            encrypted += chr((ord(char) + (2*2)) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            # Encrypt lowercase letters
            encrypted += chr((ord(char) + (2*2)) % 26 + 97)
        else:
            # Leave non-alphabetic characters as they are
            encrypted += char
    return encrypted
