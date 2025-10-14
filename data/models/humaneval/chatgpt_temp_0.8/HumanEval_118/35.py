def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    last_consonant_index = None
    for i in range(len(word)-1, 0, -1):
        if word[i] in consonants:
            last_consonant_index = i
            break
    if last_consonant_index is None:
        return ""
    for i in range(last_consonant_index-1, 0, -1):
        if word[i] in vowels:
            return word[i]
    return ""
