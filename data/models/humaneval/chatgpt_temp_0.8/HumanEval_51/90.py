def remove_vowels(text):
    vowels = 'aeiouAEIOU'  # define a string of vowels
    result = ''  # initialize an empty string to hold the result
    for char in text:
        if char not in vowels:  # if the character is not a vowel
            result += char  # add it to the result string
    return result
