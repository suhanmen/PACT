def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = word.lower()
    consonant_index = -1
    closest_vowel = ''
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels and consonant_index == -1:
            consonant_index = i
        elif word[i] in vowels and consonant_index != -1:
            closest_vowel = word[i]
            break
    return closest_vowel.upper() if closest_vowel else closest_vowel
