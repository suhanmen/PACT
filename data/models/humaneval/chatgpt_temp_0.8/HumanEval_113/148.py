def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    for s in lst:
        odd_count = sum(1 for c in s if int(c) % 2 == 1)
        result.append("the number of odd elements in the str{}ng {} of the {}nput.".format(s, odd_count, s))
    return result
