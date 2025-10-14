def get_closest_vowel(word):
    vowels = set("aeiouAEIOU") # set of vowels, case sensitive
    consonant_found = False
    closest_vowel = ""
    for i in range(len(word)-2, 0, -1): # looping from right to left, excluding the first and last characters
        if word[i] in vowels: # if current character is a vowel
            if consonant_found: # if a consonant was already found before this vowel
                closest_vowel = word[i] # update closest_vowel
                break # no need to look further
        elif not consonant_found: # if current character is a consonant and no consonant was found before
            consonant_found = True # update consonant_found
    return closest_vowel
