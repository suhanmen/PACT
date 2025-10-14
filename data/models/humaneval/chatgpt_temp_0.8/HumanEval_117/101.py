def select_words(s, n):
    # Check if the input string is empty
    if not s:
        return []
    # Split the string into words
    words = s.split()
    # Initialize an empty list to store the result
    result = []
    # Loop over the words and count the number of consonants
    for word in words:
        # Initialize a counter for consonants
        consonant_count = 0
        for letter in word:
            # Check if the letter is a consonant (i.e. not a vowel)
            if letter.lower() not in "aeiou":
                consonant_count += 1
        # If the number of consonants matches the target, add the word to the result list
        if consonant_count == n:
            result.append(word)
    # Return the result list
    return result
