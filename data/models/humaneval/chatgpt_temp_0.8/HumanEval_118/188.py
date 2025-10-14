def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    vowels_found = []
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            vowels_found.append(word[i])
        elif word[i] not in vowels and word[i+1] in vowels and word[i-1] not in vowels:
            return word[i+1]
    return ""
