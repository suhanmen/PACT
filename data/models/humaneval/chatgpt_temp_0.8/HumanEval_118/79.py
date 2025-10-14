def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(x) for x in range(ord('a'), ord('z')+1)]) - vowels

    # start from the right end of the word
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            # check if the previous and next characters are consonants
            if word[i-1] in consonants and word[i+1] in consonants:
                return word[i]

    # no vowel found between two consonants
    return ""
