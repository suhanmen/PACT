def anti_shuffle(s):
    words = s.split()  # split the string into a list of words
    result = []  # initialize an empty list to store the ordered words

    for word in words:
        ordered_chars = ''.join(sorted(word))  # sort the characters in the word
        result.append(ordered_chars)  # add the ordered word to the list

    return ' '.join(result)  # join the ordered words with spaces and return the result
