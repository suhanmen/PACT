def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    result = []
    for string in lst:
        count = 0
        for character in string:
            if int(character) % 2 == 1:  # check if character is odd
                count += 1
        result.append("the number of odd elements in the string " + string + " of the input.")
    return result
