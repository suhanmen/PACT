def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    last_consonant = None
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels:
            last_consonant = i
        elif word[i] in vowels and last_consonant is not None:
            return word[i] 
    return ""
