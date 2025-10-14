def anti_shuffle(s):
    words = s.split() # split the string into a list of words
    ordered_words = [] # create an empty list to store the ordered words
    for word in words:
        ordered_chars = sorted(word, key=lambda c: ord(c)) # sort the characters in each word by their ASCII value
        ordered_word = ''.join(ordered_chars) # join the ordered characters back into a word
        ordered_words.append(ordered_word) # add the ordered word to the list of ordered words
    ordered_sentence = ' '.join(ordered_words) # join the ordered words back into a sentence
    return ordered_sentence
