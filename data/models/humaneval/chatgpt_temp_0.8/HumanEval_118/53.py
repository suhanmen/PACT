def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = []
    for i in range(len(word) - 1, 0, -1):
        if word[i] not in vowels:
            consonants.append(word[i])
        else:
            for j in range(len(consonants) - 1, -1, -1):
                if consonants[j] in vowels:
                    return consonants[j]
            break
    return ""
