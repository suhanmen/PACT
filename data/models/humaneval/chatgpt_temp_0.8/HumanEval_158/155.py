def find_max(words):
    # Initialize variables for storing the maximum number of unique characters and the corresponding word
    max_unique_chars = 0
    max_word = ""

    # Loop through each word in the list
    for word in words:
        # Use set() to get the unique characters in the word, and len() to count them
        unique_chars = len(set(word))

        # If the current word has more unique characters than the current maximum, or if it has the same
        # number of unique characters but comes before the current maximum lexicographically, update the maximums
        if unique_chars > max_unique_chars or (unique_chars == max_unique_chars and word < max_word):
            max_unique_chars = unique_chars
            max_word = word

    # Return the word with the maximum number of unique characters
    return max_word
