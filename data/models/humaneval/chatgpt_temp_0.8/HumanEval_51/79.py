def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    """
    vowels = 'aeiouAEIOU' # define the vowels to remove
    new_text = '' # initialize new_text variable
    for char in text: # loop through each character in the input text
        if char not in vowels: # if the character is not a vowel
            new_text += char # add the character to the new_text variable
    return new_text # return the string without vowels
