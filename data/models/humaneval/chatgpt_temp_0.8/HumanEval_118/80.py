def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    found_vowel = False
    last_consonant = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] in consonants:
            last_consonant = i
        elif word[i] in vowels and last_consonant is not None:
            found_vowel = True
            return word[i]
    if not found_vowel:
        return ""
