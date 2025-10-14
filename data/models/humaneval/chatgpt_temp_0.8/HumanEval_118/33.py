def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    word = word.lower()
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i-2] in vowels:
            return word[i].upper() if word[i].isupper() else word[i]
    return ""
