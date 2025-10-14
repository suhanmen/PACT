def anti_shuffle(s):
    words = s.split()  # split string into words
    result = []  # to store the ordered words
    for word in words:
        ordered_chars = sorted(list(word), key=lambda x: ord(x))  # sort characters in the word based on ascii value
        ordered_word = ''.join(ordered_chars)  # join the ordered characters
        result.append(ordered_word)  # add the ordered word to result list
    return ' '.join(result)  # join the ordered words with space and return as string
