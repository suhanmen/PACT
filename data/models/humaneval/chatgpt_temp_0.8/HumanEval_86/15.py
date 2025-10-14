def anti_shuffle(s):
    # split the string into a list of words
    words = s.split()

    # loop through each word and sort the characters based on ascii value
    for i, word in enumerate(words):
        words[i] = ''.join(sorted(word))

    # join the sorted words back into a string
    sorted_s = ' '.join(words)

    return sorted_s
