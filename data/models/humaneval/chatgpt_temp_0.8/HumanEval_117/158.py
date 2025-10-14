def select_words(s, n):
    # First, we split the input string into a list of words
    words = s.split()
    # Then, we initialize an empty list to store the selected words
    selected = []
    # We iterate over each word
    for word in words:
        # We count the number of consonants in the word
        consonants = 0
        for letter in word:
            if letter.lower() not in "aeiou":
                consonants += 1
        # If the number of consonants matches the target, we add the word to the selected list
        if consonants == n:
            selected.append(word)
    # Finally, we return the selected list
    return selected
