def get_closest_vowel(word):
    vowels = set(['a','e','i','o','u','A','E','I','O','U'])
    found_consonant = False
    closest_vowel = ''
    for i in range(len(word)-2, 0, -1):
        if word[i] not in vowels and found_consonant:
            break
        elif word[i] in vowels and found_consonant:
            closest_vowel = word[i]
            break
        elif word[i] not in vowels and not found_consonant:
            found_consonant = True
    return closest_vowel
