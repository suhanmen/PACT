def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    word = word.lower()

    # Iterate through the characters in the word from right to left
    for i in range(len(word)-2, 0, -1):
        # If the current character is a consonant
        if word[i] in consonants:
            # Check if the previous character is a vowel
            if word[i-1] in vowels:
                # Return the closest vowel that stands between two consonants
                for j in range(i-2, 0, -1):
                    if word[j] in vowels:
                        return word[j].upper() if word[i-1].isupper() else word[j]
                return ""
    return ""
