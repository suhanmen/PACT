def anti_shuffle(s):
    # Split the string into a list of words
    words = s.split()

    # Create an empty list to store the ordered words
    ordered_words = []

    # Loop through each word in the list
    for word in words:
        # Sort the characters of the word in ascending order based on ascii value
        ordered_word = "".join(sorted(word))

        # Add the ordered word to the list of ordered words
        ordered_words.append(ordered_word)

    # Combine the ordered words back into a string, keeping the original order and spaces
    ordered_string = " ".join(ordered_words)

    return ordered_string
