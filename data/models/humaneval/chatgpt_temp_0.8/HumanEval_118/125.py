def get_closest_vowel(word):
    vowels = set('AEIOUaeiou')
    # Iterate over the characters in reverse order from the second to the second to the last
    for i in range(len(word)-2, 0, -1):
        # If the current character is a consonant and the previous and next characters are vowels
        if word[i] not in vowels and word[i-1] in vowels and word[i+1] in vowels:
            return word[i]
    # If no vowel met the above condition
    return ""
