def odd_count(lst):
    result = []
    for s in lst:
        count = sum([1 for c in s if int(c) % 2 != 0])
        result.append("the number of odd elements in the string " + s + " of the input.")
    return result
