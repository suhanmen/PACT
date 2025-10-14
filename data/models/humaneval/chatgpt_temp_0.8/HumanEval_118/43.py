def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    idx = -1
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            idx = i
        elif word[i] in consonants and idx != -1:
            return word[idx]
    return ""
