def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_consonant_index = None
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels and last_consonant_index is None:
            last_consonant_index = i
        elif word[i] in vowels and last_consonant_index is not None:
            return word[i]
    return ""
