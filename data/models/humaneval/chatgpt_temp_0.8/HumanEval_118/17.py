def get_closest_vowel(word):
    vowels = set("aeiouAEIOU")
    right_consonants = ""
    for letter in word[::-1]:
        if letter not in vowels:
            right_consonants += letter
        else:
            break
    for letter in right_consonants[::-1]:
        if letter in vowels:
            return letter
    return ""
