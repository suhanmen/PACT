def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    word = word[::-1]
    for i in range(1, len(word) - 1):
        if word[i] in vowels and not word[i-1] in vowels and not word[i+1] in vowels:
            return word[i]
    return ""
