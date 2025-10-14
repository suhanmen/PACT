def remove_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # create a list of vowels
    result = ""
    # create an empty string to store the result
    for char in text:
        if char not in vowels:
            result += char
    # iterate through each character in the text and add it to the result string if it's not a vowel
    return result
    # return the result string
