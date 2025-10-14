def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    found_vowel = False
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            found_vowel = True
            break
        elif word[i] not in vowels and word[i+1] in vowels and word[i-1] not in vowels:
            found_vowel = True
            break
    if found_vowel:
        return word[i]
    else:
        return ""
