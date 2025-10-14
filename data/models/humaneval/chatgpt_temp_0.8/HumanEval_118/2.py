def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    vowel_positions = [i for i, c in enumerate(word) if c in vowels]
    if len(vowel_positions) < 2:
        return ""
    closest_vowel = ""
    for i in range(len(vowel_positions) - 1):
        consonant_positions = [j for j in range(vowel_positions[i] + 1, vowel_positions[i + 1]) 
                              if word[j] in consonants]
        if len(consonant_positions) > 0:
            closest_vowel = max(closest_vowel, word[vowel_positions[i]], word[vowel_positions[i + 1]])
    return closest_vowel
