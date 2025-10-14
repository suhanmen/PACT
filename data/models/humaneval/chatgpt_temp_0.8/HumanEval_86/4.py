def anti_shuffle(s):
    words = s.split()  # split the string into words
    ordered_words = []
    for word in words:
        ordered_words.append(''.join(sorted(word)))  # sort the characters in each word and join them back
    return ' '.join(ordered_words)  # join the ordered words back into a string with spaces
