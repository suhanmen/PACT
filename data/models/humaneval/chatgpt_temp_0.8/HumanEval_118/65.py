def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set([chr(x) for x in range(ord('a'), ord('z')+1)]) - vowels
    
    closest_vowel = ""
    found_vowel = False
    
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i+1] in consonants and word[i-1] in consonants:
            closest_vowel = word[i]
            found_vowel = True
            break
    
    return closest_vowel if found_vowel else ""
