def anti_shuffle(s):
    words = s.split()  # Split the string into words
    ordered_words = []
    for word in words:
        # Sort the characters in the word based on their ascii value
        ordered_word = ''.join(sorted(word, key=lambda x: ord(x)))
        ordered_words.append(ordered_word)
    # Join the ordered words with the original spaces to form the final string
    return ' '.join(ordered_words)
