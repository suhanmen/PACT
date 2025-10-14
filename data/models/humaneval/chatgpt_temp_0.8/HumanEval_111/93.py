def histogram(test):
    """
    Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count. 
    If several letters have the same occurrence, return all of them.
    """
    counts = {}
    for char in test.split():
        counts[char] = counts.get(char, 0) + 1
    max_count = max(counts.values())
    return {char: count for char, count in counts.items() if count == max_count}
