def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    last_cons_idx = len(word) - 1
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i+1] in vowels:
            return word[i+1]
    return ""
