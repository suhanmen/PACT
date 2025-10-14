def get_closest_vowel(word):
    vowels = set('AEIOUaeiou')
    # iterate over the word from right to left
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels: # if a vowel is found
            for j in range(i-1, 0, -1): # iterate over the substring to the left of the vowel
                if word[j] not in vowels: # if a consonant is found
                    return word[i] # return the found vowel
    return "" # if no vowel found, return empty string
