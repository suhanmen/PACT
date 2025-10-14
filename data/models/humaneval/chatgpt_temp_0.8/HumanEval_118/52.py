def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    # Iterate over the characters of the word from the right side
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            # Check if the characters on both sides are consonants
            if word[i-1] in consonants and word[i+1] in consonants:
                return word[i]
    return ""
