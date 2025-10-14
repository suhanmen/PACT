def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    found_consonant = False
    closest_vowel = ""
    for i in range(len(word)-2, 0, -1):
        if word[i] in consonants and word[i+1] in vowels:
            found_consonant = True
            closest_vowel = word[i+1]
            break
    if not found_consonant:
        return ""
    return closest_vowel
