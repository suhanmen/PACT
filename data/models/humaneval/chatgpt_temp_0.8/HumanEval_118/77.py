def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    found_consonant = False

    for i in range(len(word)-2, 0, -1):
        if word[i] in consonants:
            found_consonant = True
        elif word[i] in vowels and found_consonant:
            return word[i]

    return ""
