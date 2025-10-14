def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    last_cons_idx = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i+1] not in vowels:
            last_cons_idx = i
        elif last_cons_idx is not None:
            return word[i]
    return ""
