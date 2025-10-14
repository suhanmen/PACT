def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    last_consonant_index = len(word) - 1
    while last_consonant_index > 0 and (word[last_consonant_index] in vowels or not word[last_consonant_index].isalpha()):
        last_consonant_index -= 1
    if last_consonant_index == 0:
        return ""
    for i in range(last_consonant_index - 1, 0, -1):
        if word[i] in vowels:
            return word[i]
    return ""
