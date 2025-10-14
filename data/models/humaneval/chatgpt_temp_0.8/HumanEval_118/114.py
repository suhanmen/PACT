def get_closest_vowel(word):
    vowels = {"a", "e", "i", "o", "u"}
    last_consonant = None
    closest_vowel = ""
    for char in word[::-1]:
        if char in vowels:
            if last_consonant is not None and closest_vowel == "":
                closest_vowel = char
            else:
                break
        elif char.isalpha():
            last_consonant = char
    return closest_vowel
