python
def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    right_consonants = []
    for i in range(len(word)-1, 0, -1):
        if word[i] not in vowels:
            right_consonants.append(word[i])
        else:
            if right_consonants:
                return word[i]
    return ""
