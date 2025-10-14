def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    last_consonant_index = -1
    closest_vowel_index = -1
    
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels:
            last_consonant_index = i
        elif word[i] in vowels and last_consonant_index != -1:
            closest_vowel_index = i
            break
    
    if closest_vowel_index != -1:
        return word[closest_vowel_index]
    else:
        return ""
