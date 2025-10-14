def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    found_consonant = False
    closest_vowel = ''
    for letter in word[::-1]:
        if letter in vowels:
            if found_consonant:
                closest_vowel = letter
                break
        else:
            found_consonant = True
    return closest_vowel
