def odd_count(lst):
    result = []
    for s in lst:
        count = 0
        for ch in s:
            if int(ch) % 2 != 0:
                count += 1
        result.append("the number of odd elements in the string {} of the input.".format(count, s))
    return result
