def unique_digits(x):
    """
    Given a list of positive integers x, return a sorted list of all 
    elements that haven't any even digit.

    Note: Returned list should be sorted in increasing order.
    """
    result = []
    for i in x:
        even = False
        for j in str(i):
            if int(j) % 2 == 0:
                even = True
                break
        if not even:
            result.append(i)
    return sorted(result)
