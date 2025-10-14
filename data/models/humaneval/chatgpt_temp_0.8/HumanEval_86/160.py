def anti_shuffle(s):
    # Split the string into a list of words
    words = s.split()

    # Create a list to hold the ordered words
    ordered_words = []

    # Loop through each word in the original list
    for word in words:
        # Sort the characters in the word based on their ascii value
        sorted_chars = sorted(word, key=lambda x: ord(x))

        # Join the sorted characters back into a string
        ordered_word = ''.join(sorted_chars)

        # Add the ordered word to the list
        ordered_words.append(ordered_word)

    # Join the ordered words back together into a string
    ordered_s = ' '.join(ordered_words)

    return ordered_s
