def histogram(test):
    # Initialize an empty dictionary to store the counts
    counts = {}
    # Split the input string into individual letters
    letters = test.split()
    # Loop over the letters and count their occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    # Find the maximum count
    max_count = max(counts.values())
    # Initialize an empty list to store the letters with maximum count
    max_letters = []
    # Loop over the counts and add any letters with maximum count to the list
    for letter, count in counts.items():
        if count == max_count:
            max_letters.append(letter)
    # Construct the output dictionary
    output = {}
    for letter in max_letters:
        output[letter] = max_count
    return output
