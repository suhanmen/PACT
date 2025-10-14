def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(x) for x in range(ord('a'), ord('z')+1)]) - vowels

    # Check if the length of the word is less than 4
    if len(word) < 4:
        return ""

    # Iterate from the right side of the word
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            # Check if the vowel is between two consonants
            if word[i-1] in consonants and word[i+1] in consonants:
                return word[i]

    return ""
