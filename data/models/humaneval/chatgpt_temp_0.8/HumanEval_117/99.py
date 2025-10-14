def select_words(s, n):
    # Initialize an empty list to store the selected words
    selected_words = []
    
    # Split the input string into words
    words = s.split()
    
    # Iterate over the words and count the number of consonants in each word
    for word in words:
        num_consonants = 0
        for letter in word:
            if letter.lower() not in "aeiou" and letter.isalpha():
                num_consonants += 1
        
        # If the word contains exactly n consonants, add it to the list of selected words
        if num_consonants == n:
            selected_words.append(word)
    
    # Return the list of selected words
    return selected_words
