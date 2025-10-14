def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            return word[i]
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] not in vowels:
            return ''
    return ''
