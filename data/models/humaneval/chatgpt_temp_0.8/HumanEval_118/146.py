def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    word = word.strip()
    n = len(word)
    i = n - 2
    while i > 0:
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels and word[i-1] in vowels and word[i+1] not in vowels:
            return ""
        i -= 1
    return ""
