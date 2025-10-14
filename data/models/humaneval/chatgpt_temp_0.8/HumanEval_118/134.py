def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(i) for i in range(ord('a'), ord('z')+1)]) - vowels
    
    # remove any leading or trailing vowels from the word
    while len(word) > 0 and word[0] in vowels:
        word = word[1:]
    while len(word) > 0 and word[-1] in vowels:
        word = word[:-1]
    
    # iterate through the word from the right side
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] in consonants and word[i+1] in vowels and word[i-1] in consonants:
            return word[i]
    
    return ""
