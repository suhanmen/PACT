def anti_shuffle(s):
    words = s.split()  # split the string into words
    new_sentence = []
    for word in words:
        new_word = ''.join(sorted(word))  # sort the characters in the word
        new_sentence.append(new_word)
    return ' '.join(new_sentence)  # join the words with spaces and return the new sentence
