def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word, key=ord))  # sort the characters in each word based on ascii value
        ordered_words.append(ordered_word)
    return ' '.join(ordered_words)  # join the ordered words with spaces and return the final string
