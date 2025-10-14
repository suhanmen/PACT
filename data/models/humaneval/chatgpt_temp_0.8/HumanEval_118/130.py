def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    consonants = set(word) - vowels
    closest_vowel = ""
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i+1] in consonants and word[i-1] in consonants:
            closest_vowel = word[i]
            break
    return closest_vowel
