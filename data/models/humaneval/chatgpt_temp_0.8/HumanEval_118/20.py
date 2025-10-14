def get_closest_vowel(word):
    # Convert the word to lowercase to handle case-insensitivity
    word = word.lower()
    
    # Iterate over the characters in reverse order
    for i in range(len(word)-2, 0, -1):
        if word[i] in "aeiou":
            # Check if the previous and next characters are consonants
            if word[i-1] not in "aeiou" and word[i-1].isalpha() and word[i+1] not in "aeiou" and word[i+1].isalpha():
                # Return the vowel if it meets the condition
                return word[i]
    
    # Return an empty string if no vowel met the condition
    return ""
