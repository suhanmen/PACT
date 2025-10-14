def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    closest_vowel = ""

    # Iterate from the right side of the word
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            # Check if the vowel is between two consonants
            if word[i-1] not in vowels and word[i+1] not in vowels:
                closest_vowel = word[i]
                break

    return closest_vowel
