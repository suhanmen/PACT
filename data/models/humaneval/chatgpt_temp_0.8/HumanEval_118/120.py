def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(x) for x in range(ord('a'), ord('z')+1)]) - vowels
    word = word.lower()

    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] in consonants and word[i+1] in vowels and word[i-1] in consonants:
            return word[i]

    return ""
