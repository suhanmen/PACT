def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    last_vowel = ""
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            last_vowel = word[i]
        elif word[i] in consonants and last_vowel != "":
            return last_vowel
    return ""
