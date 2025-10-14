def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'])
    right_consonant_found = False
    closest_vowel = ""
    for i in range(len(word) - 2, 0, -1):
        if right_consonant_found and word[i] in vowels:
            closest_vowel = word[i]
            break
        if word[i] in consonants:
            right_consonant_found = True
    return closest_vowel
