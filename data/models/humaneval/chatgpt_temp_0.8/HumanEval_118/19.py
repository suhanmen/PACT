def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set()
    closest_vowel = ''

    # Find the closest vowel that stands between two consonants from the right side of the word
    for i in range(len(word)-2, 0, -1):
        if word[i] in vowels:
            for j in range(i-1, 0, -1):
                if word[j] not in vowels:
                    consonants.add(word[j])
                else:
                    closest_vowel = word[i]
                    break
            break

    # Return empty string if no vowel met the above condition
    if not closest_vowel:
        return ''

    # Check if the closest vowel is uppercase
    if closest_vowel.isupper():
        vowels = {v.upper() for v in vowels}

    # Check if the closest vowel is in between two consonants from the right side of the word
    if closest_vowel in vowels and len(consonants) >= 2:
        return closest_vowel
    else:
        return ''
