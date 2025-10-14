def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    for string in lst:
        count = sum([1 for num in string if int(num) % 2 != 0])
        result.append(f"the number of odd elements {count}n the str{lst.index(string)+1}ng {string} of the {lst.index(string)+1}nput.")
    return result
