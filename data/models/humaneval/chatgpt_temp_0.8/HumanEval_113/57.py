def odd_count(lst):
    result = []
    for s in lst:
        odd_count = 0
        for c in s:
            if int(c) % 2 == 1:
                odd_count += 1
        result.append("the number of odd elements in the string {} of the input.".format(odd_count))
    return result
