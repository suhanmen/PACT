def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    # iterate through the word starting from the right
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels:
            # if we find a vowel between two consonants, return it
            if word[i-1] not in vowels and word[i+1] not in vowels:
                return word[i]
    # if no vowel meets the condition, return empty string
    return ""
