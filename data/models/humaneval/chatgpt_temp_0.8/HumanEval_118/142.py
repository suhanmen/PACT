def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    found_consonant = False
    for i in range(len(word) - 2, 0, -1):
        if found_consonant and word[i] in vowels:
            return word[i]
        elif not found_consonant and word[i] not in vowels:
            found_consonant = True
    return ""
