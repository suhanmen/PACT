def find_max(words):
    # Initialize variables to keep track of maximum length and corresponding word
    max_length = 0
    max_word = ""
    # Iterate over each word in the list
    for word in words:
        # Convert the word to a set to get unique characters
        unique_chars = set(word)
        # Check if this word has more unique characters than the current maximum
        if len(unique_chars) > max_length:
            max_length = len(unique_chars)
            max_word = word
        # If there are multiple words with maximum unique characters, return the one
        # that comes first in lexicographical order
        elif len(unique_chars) == max_length and word < max_word:
            max_word = word
    # Return the word with maximum unique characters
    return max_word
