def get_closest_vowel(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    last_vowel_index = -1
    for i in range(len(word)-1, 0, -1): # start from the right side of the word
        if word[i] in vowels:
            if last_vowel_index != -1 and i - last_vowel_index > 1: # found a vowel between two consonants
                return word[i]
            last_vowel_index = i
    return "" # no vowel found between two consonants
