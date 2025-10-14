def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    word = word.strip(consonants)
    closest_vowel = ""
    distance = float("inf")
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            for j in range(i - 1, 0, -1):
                if word[j] in consonants:
                    if i - j < distance:
                        closest_vowel = word[i]
                        distance = i - j
                    break
    return closest_vowel
