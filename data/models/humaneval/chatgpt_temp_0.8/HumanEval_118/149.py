def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u']) # set of vowels
    idx = len(word) - 2 # index of second last character
    while idx > 0:
        if word[idx] in vowels: # if character is a vowel
            return word[idx] # return the vowel
        elif word[idx] not in vowels and word[idx-1] in vowels and word[idx+1] not in vowels: 
            # if character is a consonant between two vowels
            return ""
        idx -= 1
    return "" # if no such vowel is found, return empty string
