def anti_shuffle(s):
    # split the input string into individual words
    words = s.split()
    # create an empty list to store the sorted words
    sorted_words = []
    # iterate over the words in the input string
    for word in words:
        # sort the characters in the word based on ascii value
        sorted_word = ''.join(sorted(word))
        # add the sorted word to the list of sorted words
        sorted_words.append(sorted_word)
    # join the sorted words back into a single string, with spaces between them
    sorted_s = ' '.join(sorted_words)
    return sorted_s
