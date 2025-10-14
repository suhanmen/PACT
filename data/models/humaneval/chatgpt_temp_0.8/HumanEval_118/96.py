def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    closest_vowel = ""
    found_vowel = False
    
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            found_vowel = True
            closest_vowel = word[i]
        elif found_vowel and word[i] not in vowels:
            return closest_vowel
            
    return ""
