def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    prev_consonant = None
    found_vowel = False
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and prev_consonant is not None:
            if found_vowel:
                return word[i]
            elif word[prev_consonant] in vowels:
                found_vowel = True
        elif word[i] in vowels:
            prev_consonant = i
    return ''
