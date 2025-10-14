def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    found_vowel = False
    for i in range(len(word)-2, 0, -1):
        if word[i] in consonants and word[i+1] in vowels and word[i-1] in consonants:
            return word[i+1]
    return ""
