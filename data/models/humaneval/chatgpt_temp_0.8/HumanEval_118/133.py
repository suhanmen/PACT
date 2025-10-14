def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    right_consonant_found = False
    vowel_found = False
    
    for i in range(len(word)-2,0,-1):
        if word[i] in vowels and right_consonant_found:
            return word[i]
        elif word[i] not in vowels:
            right_consonant_found = True
        elif word[i] in vowels:
            vowel_found = True
    
    if vowel_found and not right_consonant_found:
        return ""
    else:
        return ""
