def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    last_consonant_index = -1
    closest_vowel_index = -1

    for i in range(len(word)-1, 1, -1): # iterate from right to left
        if word[i] in vowels:
            closest_vowel_index = i
            break
        elif word[i] in consonants and last_consonant_index != -1:
            if closest_vowel_index == -1 or last_consonant_index - i < closest_vowel_index - last_consonant_index:
                closest_vowel_index = last_consonant_index
            last_consonant_index = i
        elif word[i] in consonants:
            last_consonant_index = i

    if closest_vowel_index != -1:
        return word[closest_vowel_index]
    else:
        return ""
