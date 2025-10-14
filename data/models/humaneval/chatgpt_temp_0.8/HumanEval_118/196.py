def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    right_consonants = []
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] not in vowels:
            right_consonants.append(word[i])
    if len(right_consonants) == 0:
        return ""
    else:
        closest = min(right_consonants, key=lambda x: abs(ord(x) - ord("o")))
        return closest
