def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

    # Removing the vowels in the beginning and ending of the word
    word = word[1:-1]

    # Initializing the index of the closest vowel to -1
    closest_vowel_idx = -1

    # Iterating over the characters of the word from the right side
    for i in range(len(word) - 1, 0, -1):
        if word[i] in vowels:
            # If a vowel is found, check if it is between two consonants
            if word[i - 1] in consonants and word[i + 1] in consonants:
                closest_vowel_idx = i
                break

    if closest_vowel_idx != -1:
        return word[closest_vowel_idx]
    else:
        return ""
