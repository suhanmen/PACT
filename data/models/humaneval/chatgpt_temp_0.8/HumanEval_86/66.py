def anti_shuffle(s):
    # Split the string into words
    words = s.split()

    # Iterate through each word
    for i in range(len(words)):
        # Sort the characters in the word
        sorted_word = ''.join(sorted(words[i]))

        # Replace the word in the list with the sorted word
        words[i] = sorted_word

    # Join the list of words back into a string
    result = ' '.join(words)

    return result
