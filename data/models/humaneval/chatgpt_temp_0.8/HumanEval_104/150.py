def unique_digits(x):
    """Given a list of positive integers x. Return a sorted list of all 
    elements that hasn't any even digit. The returned list should be sorted in increasing order."""
    
    result = []
    for i in x:
        string_i = str(i)
        if all(int(j) % 2 != 0 for j in string_i):
            result.append(i)
    return sorted(result)
