def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    n = len(word)
    for i in range(n-2, 0, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels and word[i+1] in vowels and word[i-1] not in vowels:
            return word[i+1]
    return ""
