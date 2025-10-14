def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    consonants = set("bcdfghjklmnpqrstvwxyz")
    word = word.lower()
    index = len(word) - 2
    while index > 0:
        if word[index] in vowels:
            return word[index].upper() if word[-1].isupper() else word[index]
        elif word[index] in consonants:
            index -= 1
        else:
            return ""
    return ""
