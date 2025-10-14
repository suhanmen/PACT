def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    found_vowel = ""
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i-2] in vowels:
            found_vowel = word[i]
            break
    return found_vowel
