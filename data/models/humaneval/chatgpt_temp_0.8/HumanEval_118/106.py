def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(i) for i in range(97, 123)]) - vowels
    # Removing the first and last character from the word
    word = word[1:-1]
    # Iterating over the characters from the right side
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i-1] in consonants:
            return word[i]
    return ""
