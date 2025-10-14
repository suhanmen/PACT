def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = word.lower()
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            continue
        if word[i-1] in vowels and word[i+1] in vowels:
            return word[i].upper() if word[i].isupper() else word[i]
    return ""
