def anti_shuffle(s):
    words = s.split()  # split the string into words
    result = []  # initialize an empty list to store the ordered words

    for word in words:
        ordered_word = "".join(sorted(word))  # sort the characters in the word
        result.append(ordered_word)  # add the ordered word to the result list

    return " ".join(result)  # join the ordered words using spaces and return as a string
