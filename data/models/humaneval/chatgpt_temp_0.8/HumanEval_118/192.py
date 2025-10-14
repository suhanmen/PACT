def get_closest_vowel(word):
    vowels = "aeiou"
    word = word.lower()[1:-1]  # exclude first and last letters
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i].upper() if word[i].isupper() else word[i]
    return ""
