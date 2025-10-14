def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    counts = {}
    # split string into a list of lowercase letters
    chars = test.lower().split()

    # count occurrences of each letter
    for char in chars:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    # find the highest count
    max_count = max(counts.values())

    # create a dictionary with the letters that have the highest count
    max_letters = {}
    for char, count in counts.items():
        if count == max_count:
            max_letters[char] = count

    return max_letters
