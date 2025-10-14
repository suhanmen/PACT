def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    reversed_word = word[::-1]
    consonant_count = 0
    for char in reversed_word:
        if char not in vowels:
            consonant_count += 1
        else:
            if consonant_count >= 2:
                return char
    return ""
