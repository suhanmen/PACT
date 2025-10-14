python
def anti_shuffle(s):
    words = s.split()  # split the string into words

    # sort each word based on the ascii value of its characters
    sorted_words = [''.join(sorted(word)) for word in words]

    # combine the sorted words back into a string, preserving the order of words and spaces
    return ' '.join(sorted_words)
