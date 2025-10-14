def odd_count(lst):
    """
    Given a list of strings, where each string consists of only digits,
    return a list where each element i is the number of odd digits in the
    i'th string of the input.

    >>> odd_count(['1234567'])
    [4]
    >>> odd_count(['3',"11111111"])
    [1, 8]
    """
    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 == 1:
                count += 1
        result.append(count)
    return result
