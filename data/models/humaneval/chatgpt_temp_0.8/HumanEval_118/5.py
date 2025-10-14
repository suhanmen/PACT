def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    found_consonant = False
    closest_vowel = ""
    
    # iterate over the characters in reverse order
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            if found_consonant:
                closest_vowel = word[i]
                break
        else:
            found_consonant = True
    
    return closest_vowel
