def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    last_consonant_index = -1
    for i in range(len(word) - 1, 0, -1):
        if word[i] not in vowels:
            last_consonant_index = i
            continue
        if last_consonant_index != -1 and i < last_consonant_index:
            return word[i]
    return ""
