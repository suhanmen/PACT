def odd_count(lst):
    result = []
    for s in lst:
        count = 0
        for c in s:
            if int(c) % 2 == 1:
                count += 1
        result.append("the number of odd elements in the string {} of the input.".format(count))
    return result
