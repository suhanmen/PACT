def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    found_vowel = False
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            found_vowel = True
        elif word[i] in consonants and found_vowel:
            return word[i]
    return ""
