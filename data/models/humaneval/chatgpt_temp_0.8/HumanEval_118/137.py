def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = []
    closest_vowel = ''
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels:
            consonants.append(word[i])
        else:
            if consonants:
                closest_vowel = word[i]
                break
    return closest_vowel
