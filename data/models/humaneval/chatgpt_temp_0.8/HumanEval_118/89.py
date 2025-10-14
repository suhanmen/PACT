def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    found_consonant = False
    closest_vowel = ""

    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and not found_consonant:
            found_consonant = True
        elif word[i] in vowels and found_consonant:
            closest_vowel = word[i]
            break

    return closest_vowel
