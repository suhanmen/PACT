def anti_shuffle(s):
    words = s.split()   # split the string into words
    new_words = []
    for word in words:
        sorted_word = ''.join(sorted(word))   # sort the characters in the word
        new_words.append(sorted_word)
    # join the new words with the original spaces between them
    return ' '.join(new_words)
