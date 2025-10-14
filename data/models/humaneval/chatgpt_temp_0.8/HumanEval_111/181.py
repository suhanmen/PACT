def histogram(test):
    # Create an empty dictionary to store the letter counts
    counts = {}

    # Split the input string into individual letters
    letters = test.split()

    # Loop through each letter and update the dictionary count
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Find the maximum count value
    max_count = max(counts.values())

    # Create a list of letters that have the maximum count value
    max_letters = [letter for letter, count in counts.items() if count == max_count]

    # Create a dictionary of the max letters and their counts
    result = {letter: count for letter, count in counts.items() if letter in max_letters}

    return result
