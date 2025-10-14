def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    for string in lst:
        odd_count = len([char for char in string if int(char) % 2 == 1])
        result.append("the number of odd elements in the str{}ng {} of the {}nput.".format(
            string,
            odd_count,
            lst.index(string)+1
        ))
    return result
