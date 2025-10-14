def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    consonants_indices = [i for i, c in enumerate(word) if c not in vowels]
    for i in range(len(consonants_indices)-1, 0, -1):
        start = consonants_indices[i-1] + 1
        end = consonants_indices[i]
        for j in range(end-1, start, -1):
            if word[j] in vowels:
                return word[j]
    return ""
