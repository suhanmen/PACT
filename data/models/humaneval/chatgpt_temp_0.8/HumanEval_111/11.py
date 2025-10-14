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
    if not test:
        return {}

    letters = test.split()
    letter_count = {}
    max_count = 0

    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

        count = letter_count[letter]
        if count > max_count:
            max_count = count

    max_letters = []
    for letter, count in letter_count.items():
        if count == max_count:
            max_letters.append(letter)

    return {letter: max_count for letter in max_letters}
