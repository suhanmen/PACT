def anti_shuffle(s):
    # Split the input string into a list of words
    words = s.split()

    # Initialize an empty list to store the ordered words
    ordered_words = []

    # Iterate over each word in the input string
    for word in words:
        # Convert the word to a list of characters
        chars = list(word)
        # Sort the characters in ascending order based on ascii value
        sorted_chars = sorted(chars, key=lambda x: ord(x))
        # Convert the sorted characters back to a string
        ordered_word = ''.join(sorted_chars)
        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)

    # Join the ordered words back into a string, preserving the original spaces
    ordered_string = ' '.join(ordered_words)

    return ordered_string
