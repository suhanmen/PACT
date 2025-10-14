def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_consonant = None
    for i in range(len(word) - 1, 0, -1):
        if word[i] not in vowels:
            if last_consonant is None:
                last_consonant = i
        else:
            if last_consonant is not None and i < last_consonant:
                return word[i]
    return ""
