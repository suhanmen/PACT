def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_consonant_idx = -1
    closest_vowel_idx = -1
    
    # iterate through the word from the right side
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            closest_vowel_idx = i
            break
        elif word[i] not in vowels and word[i+1] in vowels:
            # check if the current letter is a consonant and the next one is a vowel
            last_consonant_idx = i
    
    # if there is no vowel or there is no consonant followed by a vowel
    if closest_vowel_idx == -1 or last_consonant_idx == -1:
        return ""
    
    # find the closest vowel to the right of the last consonant
    for i in range(last_consonant_idx+1, closest_vowel_idx):
        if word[i] in vowels:
            return word[i]
    
    return "" # if no vowel found between the last consonant and the closest vowel
