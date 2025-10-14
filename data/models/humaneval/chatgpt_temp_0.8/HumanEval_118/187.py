def get_closest_vowel(word):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and word[i-1] in vowels and word[i-2] not in vowels and word[i+1] not in vowels:
            for j in range(i, len(word)):
                if word[j] in vowels:
                    return word[j]
    return ''
