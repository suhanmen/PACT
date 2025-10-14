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
    for char in test:
        if char.isalpha():
            if char not in counts:
                counts[char] = 0
            counts[char] += 1
            
    max_count = max(list(counts.values()) + [0])
    max_chars = []
    for char, count in counts.items():
        if count == max_count:
            max_chars.append(char)
        
    return {char: max_count for char in max_chars}
