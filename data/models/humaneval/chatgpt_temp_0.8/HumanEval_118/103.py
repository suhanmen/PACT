def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    last_vowel = ''
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i+1] in consonants and word[i-1] in consonants:
            last_vowel = word[i]
            break
    return last_vowel
