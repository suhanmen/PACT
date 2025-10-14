def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    found_consonant = False
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels:
            found_consonant = True
        elif found_consonant:
            return word[i]
    return ""
