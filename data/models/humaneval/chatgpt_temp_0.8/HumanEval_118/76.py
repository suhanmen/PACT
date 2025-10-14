def get_closest_vowel(word):
    vowels = set(['a', 'e', 'i', 'o', 'u']) # Set of vowels
    word = word.lower() # Convert word to lower case to make it case-insensitive
    for i in range(len(word)-2, 0, -1): # Start from second last letter and iterate backwards
        if word[i] in vowels and word[i-1] not in vowels and word[i-2] not in vowels: # Check if vowel is between two consonants
            return word[i] # Return the closest vowel
    return "" # Return empty string if no vowel was found
