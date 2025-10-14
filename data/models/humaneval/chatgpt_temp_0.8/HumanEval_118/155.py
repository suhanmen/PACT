def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            for j in range(i - 1, 0, -1):
                if word[j] not in vowels:
                    return word[i]
    return ""
