def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    idx = len(word) - 2
    while idx >= 1:
        if word[idx] in vowels:
            return word[idx]
        elif word[idx] in consonants and word[idx+1] in consonants:
            return ""
        idx -= 1
    return ""
