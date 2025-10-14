def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    :param lst: list of strings
    :return: list of strings with replaced i's by the number of odd digits in the i'th string of the input
    """
    result = []
    for i in lst:
        odd_count = sum([int(j) % 2 != 0 for j in i]) # count the number of odd digits in i
        result.append("the number of odd elements in the str{}ng {} of the {}nput.".format(i.index(i)+1, odd_count, "i"))
    return result
