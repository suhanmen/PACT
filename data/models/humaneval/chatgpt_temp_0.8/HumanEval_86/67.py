def anti_shuffle(s):
    words = s.split()  # split the string into words
    new_words = []
    for word in words:
        # sort the characters in the word based on ascii value
        sorted_word = ''.join(sorted(word, key=lambda x: ord(x)))
        new_words.append(sorted_word)
    # combine the new words into a sentence, keeping the original order of words and spaces
    new_sentence = ' '.join(new_words)
    return new_sentence
