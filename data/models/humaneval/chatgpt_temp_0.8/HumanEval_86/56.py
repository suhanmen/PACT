def anti_shuffle(s):
    # Split the string into a list of words
    words = s.split()
    # For each word in the list
    for i in range(len(words)):
        # Sort the characters in the word based on ascii value
        sorted_word = ''.join(sorted(words[i]))
        # Replace the original word with the sorted word
        words[i] = sorted_word
    # Join the words back together with spaces
    return ' '.join(words)
