def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    right_cons = []
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels and word[i+1] not in vowels:
            right_cons.append(word[i])
        elif word[i] in vowels:
            if right_cons:
                return word[i]
            else:
                return ""
    return ""
