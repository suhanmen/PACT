def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    consonants = set([chr(i) for i in range(97, 123)]) - vowels

    # remove vowels from the beginning and ending of the word
    word = word.strip(vowels)

    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i]

    return ""
