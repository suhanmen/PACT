def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns a string without vowels.
    """
    vowels = set('AEIOUaeiou')
    return ''.join(char for char in text if char not in vowels)
