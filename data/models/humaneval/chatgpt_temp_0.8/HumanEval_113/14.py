def odd_count(lst):
    result = []
    for s in lst:
        odd_count = sum(int(digit) % 2 == 1 for digit in s)
        result.append("the number of odd elements in the string {} of the input.".format(odd_count, s))
    return result
