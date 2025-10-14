def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.
    """
    output = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                count += 1
        output.append(f"the number of odd elements {count}n the str{string} of the {len(lst)}nput.")
    return output
