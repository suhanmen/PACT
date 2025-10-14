def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_consonant = ""
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and last_consonant != "":
            if word[i-1] in vowels:
                return word[i-1]
        elif word[i] in vowels:
            last_consonant = word[i]
    return ""
