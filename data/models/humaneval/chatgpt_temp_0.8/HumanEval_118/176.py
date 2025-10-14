def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    reversed_word = word[::-1]
    for i, char in enumerate(reversed_word[1:], 1):
        if char in vowels and reversed_word[i-1] not in vowels:
            for j in range(i, len(word)-1):
                if word[j] not in vowels and word[j+1] in vowels:
                    return char
            return ""
    return ""
