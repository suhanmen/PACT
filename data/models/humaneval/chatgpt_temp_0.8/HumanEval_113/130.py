def odd_count(lst):
    result = []
    for s in lst:
        odd_count = sum(int(digit) % 2 != 0 for digit in s)
        result.append("the number of odd elements in the str{}ng {} of the {}nput.".format(s.index(s)+1, odd_count, lst.index(s)+1))
    return result
