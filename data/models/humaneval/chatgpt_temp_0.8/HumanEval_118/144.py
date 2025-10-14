def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    found_vowel = False
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            found_vowel = True
        if found_vowel and word[i] not in vowels and word[i-1] in vowels:
            return word[i-1]
    return ""
