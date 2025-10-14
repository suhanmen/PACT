def odd_count(lst):
    output = []
    for string in lst:
        odd_count = sum([1 for digit in string if int(digit) % 2 == 1])
        output.append("the number of odd elements in the string {} of the input.".format(odd_count, len(string)))
    return output
