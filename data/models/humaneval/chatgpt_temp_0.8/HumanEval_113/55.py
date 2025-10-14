def odd_count(lst):
    result = []
    for s in lst:
        count = sum(int(digit) % 2 == 1 for digit in s)
        result.append("the number of odd elements in the string {} of the input.".format(count, s))
    return result
