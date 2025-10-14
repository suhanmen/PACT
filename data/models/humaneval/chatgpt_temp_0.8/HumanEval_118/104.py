def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    right_consonant_found = False
    closest_vowel = ""
    for i in range(len(word)-1, 0, -1):
        if word[i] in vowels:
            if right_consonant_found:
                return closest_vowel
            else:
                closest_vowel = word[i]
        else:
            right_consonant_found = True
    return ""
