def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    last_cons_idx = -1
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i + 1] not in vowels:
            last_cons_idx = i
        elif word[i] in vowels and last_cons_idx != -1:
            return word[i]
    return ""
