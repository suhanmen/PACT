def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    right_consonants = []
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels:
            right_consonants.append(word[i])
        if word[i] in vowels:
            if right_consonants:
                return word[i]
            else:
                return ""
    return ""
