def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    last_consonant = None
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels:
            last_consonant = word[i]
        else:
            if last_consonant is not None:
                return word[i]
    return ""
