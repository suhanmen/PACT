def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    last_consonant = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and last_consonant:
            return last_consonant
        elif word[i] in vowels:
            last_consonant = word[i]
    return ""
