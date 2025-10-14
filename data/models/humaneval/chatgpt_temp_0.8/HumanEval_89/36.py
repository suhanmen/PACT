def encrypt(s):
    # Define the rotated alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = alphabet[4:] + alphabet[:4]
    
    # Create a dictionary to map each letter to its rotated counterpart
    mapping = dict(zip(alphabet, rotated))
    
    # Use the mapping to encrypt the string
    result = ''.join(mapping.get(c, c) for c in s)
    
    return result
