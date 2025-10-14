python
def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    last_cons_idx = len(word) - 2
    for i in range(last_cons_idx, 0, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] in consonants and word[i-1] in vowels and word[i+1] in consonants:
            return ""
    return ""
