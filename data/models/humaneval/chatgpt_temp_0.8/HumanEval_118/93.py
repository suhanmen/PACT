def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    closest_vowel = ''
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            closest_vowel = word[i]
            break
    return closest_vowel
