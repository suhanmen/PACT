def anti_shuffle(s):
    # Split the input string into a list of words
    words = s.split()

    # Define a helper function to sort the characters in a word
    def sort_word(word):
        return ''.join(sorted(word))

    # Use the helper function to sort each word in the list
    sorted_words = [sort_word(word) for word in words]

    # Rejoin the sorted words into a string, keeping the original spaces
    result = ' '.join(sorted_words)

    return result
