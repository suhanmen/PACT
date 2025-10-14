def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_consonant_index = len(word) - 2
    for i in range(last_consonant_index, 0, -1):
        if word[i] in vowels:
            return word[i]
        elif word[i] not in vowels and word[i-1] in vowels and word[i+1] in vowels:
            return ""
    return ""
