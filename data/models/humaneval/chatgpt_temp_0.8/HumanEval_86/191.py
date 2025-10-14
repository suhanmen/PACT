def anti_shuffle(s):
    # Split the input string into words by spaces
    words = s.split()

    # Iterate over each word and sort the characters in ascending order based on ascii value
    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))

    # Join the sorted words back together into a string
    sorted_string = ' '.join(words)

    return sorted_string
