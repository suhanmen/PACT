def get_closest_vowel(word):
    vowels = set("aeiouAEIOU") # create a set of all vowels (both lower and upper case)
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") # create a set of all consonants (both lower and upper case)
    for i in range(len(word)-2, 0, -1): # loop through the word from right to left (excluding the first and last characters)
        if word[i] in vowels: # if a vowel is found
            for j in range(i-1, 0, -1): # loop through the characters to the left of the vowel
                if word[j] in consonants: # if a consonant is found
                    for k in range(j-1, 0, -1): # loop through the characters to the left of the consonant
                        if word[k] in vowels: # if another vowel is found
                            return word[i] # return the closest vowel that stands between two consonants
                    return "" # if no other vowel is found, return an empty string
            return "" # if no consonant is found, return an empty string
 
