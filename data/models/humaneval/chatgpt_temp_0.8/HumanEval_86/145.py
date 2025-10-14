def anti_shuffle(s):
    # Split the string into a list of words
    words = s.split()
    # Iterate through each word in the list
    for i in range(len(words)):
        # Convert each word into a sorted list of characters based on ASCII value
        sorted_chars = sorted(words[i], key=lambda c: ord(c))
        # Join the sorted characters back into a string
        sorted_word = ''.join(sorted_chars)
        # Replace the original word with the sorted word
        words[i] = sorted_word
    # Join the list of words back into a string, separated by spaces
    return ' '.join(words)
