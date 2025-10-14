def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(i) for i in range(ord('b'), ord('z')+1)]) - vowels
    word = word.lower()
    
    # find the closest vowel that stands between two consonants from the right side
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] in consonants and word[i+1] in consonants:
            return word[i].upper() if word[i].isupper() else word[i]
    
    # return empty string if no such vowel is found
    return ""
