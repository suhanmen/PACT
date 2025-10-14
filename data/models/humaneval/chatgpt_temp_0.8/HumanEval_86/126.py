def anti_shuffle(s):
    # Split the input string into words
    words = s.split()
    # Define a helper function to sort the characters in a word
    def sort_word(word):
        return ''.join(sorted(word))
    # Apply the helper function to each word and join them back
    ordered_words = [sort_word(word) for word in words]
    return ' '.join(ordered_words)
