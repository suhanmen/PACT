def get_closest_vowel(word):
    vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    index = len(word) - 2
    while index > 0:
        if word[index] in vowel_set:
            return word[index]
        if word[index] not in vowel_set and word[index + 1] in vowel_set:
            return ""
        index -= 1
    return ""
