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
    # Define a list of vowels to be removed from the input string
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize an empty string to store the result
    result = ""
    
    # Iterate over each character in the input string
    for char in text:
        # If the character is not a vowel, add it to the result string
        if char.lower() not in vowels:
            result += char
    
    # Return the result string
    return result
