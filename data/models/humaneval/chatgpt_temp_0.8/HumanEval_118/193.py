def get_closest_vowel(word):
    vowels = "AEIOUaeiou"  # all possible vowels
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"  # all possible consonants
    found_vowel = False  # flag for checking if we have found a vowel
    for i in range(len(word)-2, 0, -1):  # start from the second last letter (ignore first and last letters)
        if word[i] in vowels:  # if the letter is a vowel
            found_vowel = True  # set the flag to True
            for j in range(i-1, 0, -1):  # start from the previous letter
                if word[j] in consonants:  # if the letter is a consonant
                    return word[i]  # return the closest vowel between two consonants
    if not found_vowel:  # if no vowel was found
        return ""  # return empty string
