def anti_shuffle(s):
    # split the string into words
    words = s.split()

    # sort each word in ascending order based on ascii value
    sorted_words = [''.join(sorted(word)) for word in words]

    # join the sorted words back together with their original spaces
    return ' '.join(sorted_words)
