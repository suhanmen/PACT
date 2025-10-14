def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    right_consonants = []
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels:
            right_consonants.append(word[i])
        else:
            if len(right_consonants) > 0:
                return word[i]
    return ""
