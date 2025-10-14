def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set([chr(x) for x in range(ord('a'), ord('z')+1)]) - vowels
    
    # Remove vowels in the beginning and ending
    word = word.strip(vowels)
    
    closest_vowel = ""
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i-1] in consonants:
            closest_vowel = word[i]
            break
    
    return closest_vowel
