def get_closest_vowel(word):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    right_consonants = []
    for i in range(len(word) - 2, 0, -1):
        if word[i] not in vowels:
            right_consonants.append(word[i])
        else:
            return min([c for c in right_consonants if c > word[i]]) if right_consonants else ""
    return ""
