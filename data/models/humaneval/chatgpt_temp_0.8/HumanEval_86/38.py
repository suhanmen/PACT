def anti_shuffle(s):
    words = s.split()  # split the input string into words
    ordered_words = []
    for word in words:
        ordered_word = ''.join(sorted(word))  # sort the characters in each word and join them back into a string
        ordered_words.append(ordered_word)
    ordered_sentence = ' '.join(ordered_words)  # join the ordered words back into a sentence
    return ordered_sentence
