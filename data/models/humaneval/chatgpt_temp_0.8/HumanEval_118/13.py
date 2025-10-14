def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    # We start iterating from the second last character
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            # If the character is a vowel, we check if the previous 
            # character is a consonant and the next character is also a 
            # consonant
            if (word[i-1] not in vowels) and (word[i+1] not in vowels):
                return word[i]
    # We couldn't find any vowel that met the above condition, so we return an empty string
    return ""
