def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    last_vowel_index = None
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            last_vowel_index = i
        elif last_vowel_index is not None and word[i] not in vowels:
            return word[last_vowel_index]
    return ""
