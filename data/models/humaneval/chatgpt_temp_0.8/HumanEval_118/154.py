def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    last_vowel = ''
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            last_vowel = word[i]
            break
    return last_vowel
