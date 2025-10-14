def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    vowels_found = []
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels:
            vowels_found.append(word[i])
        if len(vowels_found) == 1:
            return vowels_found[0]
    return ""
