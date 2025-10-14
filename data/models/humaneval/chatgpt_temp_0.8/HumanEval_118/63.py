def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    last_cons_pos = None
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i+1] not in vowels:
            last_cons_pos = i
        elif word[i] in vowels:
            if last_cons_pos is not None:
                return word[i]
            else:
                break
    return ""
