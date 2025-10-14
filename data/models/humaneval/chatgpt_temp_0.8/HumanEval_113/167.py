def odd_count(lst):
    output = []
    for s in lst:
        odd_count = len([c for c in s if int(c) % 2 == 1])
        output.append("the number of odd elements in the string {} of the input.".format(odd_count, s))
    return output
