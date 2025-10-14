def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements in the string 1 of the input."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements in the string 1 of the input.",
     "the number of odd elements in the string 8 of the input."]
    """
    output = []
    for num_str in lst:
        num_odds = len([x for x in num_str if int(x) % 2 == 1])
        output.append(f"the number of odd elements in the string {num_odds} of the input.")
    return output
