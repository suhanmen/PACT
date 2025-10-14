def get_closest_vowel(word):
    vowels = "aeiouAEIOU"
    # Check if the word is long enough to contain vowels between two consonants
    if len(word) > 2:
        # Iterate over the characters in the word from right to left
        for i in range(len(word)-2, 0, -1):
            # Check if the current character is a consonant and the next character is a vowel
            if word[i] not in vowels and word[i-1] in vowels and word[i-2] not in vowels:
                return word[i-1]
    # If no vowel is found, return an empty string
    return ""
