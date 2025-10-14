def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    for string in lst:
        count = sum(int(num) % 2 == 1 for num in string)
        result.append("the number of odd elements in the string {} of the input.".format(count))
    return result
