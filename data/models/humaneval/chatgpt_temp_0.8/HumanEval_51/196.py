python
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = "aeiouAEIOU"  # Define list of vowels
    new_text = ""         # Create empty string
    for char in text:     # Iterate through each character in the input text
        if char not in vowels:  # Check if the character is not a vowel
            new_text += char    # If it is not a vowel, add it to the new string
    return new_text        # Return the new string with vowels removed
