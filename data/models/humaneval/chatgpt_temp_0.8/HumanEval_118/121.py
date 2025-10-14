def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = word.lower()
    last_consonant = None
    for i in range(len(word)-2, 0, -1):
        char = word[i]
        if char in vowels:
            if last_consonant is not None and last_consonant - i > 1:
                return char.upper() if word[i].isupper() else char
        elif char.isalpha():
            last_consonant = i
    return ""
