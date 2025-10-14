def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    vowels = "aeiouAEIOU"  # define a string with all vowels
    result = ""  # initialize an empty string to store the result
    for char in text:  # iterate over each character in the input text
        if char not in vowels:  # if the character is not a vowel, add it to the result string
            result += char
    return result  # return the result string
