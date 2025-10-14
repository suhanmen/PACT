def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = word.lower()
    n = len(word)

    for i in range(n-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i].upper()

    return ""
