def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    last_vowel_index = -1
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            last_vowel_index = i
        elif last_vowel_index != -1:
            return word[last_vowel_index]
    return ""
