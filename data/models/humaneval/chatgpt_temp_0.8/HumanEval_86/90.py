def anti_shuffle(s):
    words = s.split()  # split the string into words
    result = []  # initialize an empty list to hold the ordered words
    for word in words:
        ordered_chars = sorted(word, key=lambda x: ord(x))  # sort the characters in the word
        ordered_word = ''.join(ordered_chars)  # join the characters back into a string
        result.append(ordered_word)  # add the ordered word to the result list
    return ' '.join(result)  # join the ordered words back into a string with spaces between them
