def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    i = len(word) - 2
    
    while i > 0:
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
        i -= 1
    
    return ""
