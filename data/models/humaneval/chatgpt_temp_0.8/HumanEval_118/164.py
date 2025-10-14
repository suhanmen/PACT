def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    closest_vowel_idx = -1

    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            closest_vowel_idx = i
            break
        elif word[i] not in vowels and word[i - 1] in vowels and word[i + 1] not in vowels:
            closest_vowel_idx = i - 1 # check for the closest vowel that stands between two consonants from right side
            break

    if closest_vowel_idx == -1:
        return ""
    else:
        return word[closest_vowel_idx]
