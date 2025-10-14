def get_closest_vowel(word):
    vowels = set("AEIOUaeiou")
    consonants = set("BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz")
    right_most_vowel = ""
    found_vowel = False
    for i in range(len(word)-2,0,-1):
        if word[i] in vowels:
            found_vowel = True
            right_most_vowel = word[i]
        elif word[i] in consonants and found_vowel:
            return right_most_vowel.upper() if right_most_vowel.islower() else right_most_vowel
    return ""
