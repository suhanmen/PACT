def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []  # initialize a list to hold ordered versions of words

    # loop through each word and order its characters
    for word in words:
        ordered_word = ''.join(sorted(word))
        ordered_words.append(ordered_word)

    # join the ordered words with the original spaces between them
    return ' '.join(ordered_words)
