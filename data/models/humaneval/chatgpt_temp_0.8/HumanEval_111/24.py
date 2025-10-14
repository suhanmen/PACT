def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    """
    # Initialize an empty dictionary to store the counts of each letter
    counts = {}

    # Split the input string into individual letters
    letters = test.split()

    # Loop through each letter and count its occurrences
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    # Find the maximum count
    max_count = max(counts.values())

    # Initialize an empty dictionary to store the letters with the maximum count
    max_letters = {}

    # Loop through each letter and add it to the max_letters dictionary
    # if its count is equal to the maximum count
    for letter, count in counts.items():
        if count == max_count:
            max_le
