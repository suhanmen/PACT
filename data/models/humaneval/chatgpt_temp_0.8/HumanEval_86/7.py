def anti_shuffle(s):
    # Split the string into words
    words = s.split()

    # Sort the characters in each word and join them back
    sorted_words = [''.join(sorted(word)) for word in words]

    # Combine the sorted words back into a string
    return ' '.join(sorted_words)
