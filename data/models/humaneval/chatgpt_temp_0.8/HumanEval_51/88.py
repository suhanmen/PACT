def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    vowels = "aeiouAEIOU"
    result = ""
    for letter in text:
        if letter not in vowels:
            result += letter
    return result
