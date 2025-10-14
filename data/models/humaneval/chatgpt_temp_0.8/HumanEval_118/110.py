def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    reversed_word = word[::-1]
    last_consonant_index = None
    for i, char in enumerate(reversed_word[1:], start=1):
        if char not in vowels and reversed_word[i-1] in vowels:
            last_consonant_index = i
        elif char in vowels and last_consonant_index is not None:
            return char

    return ""
