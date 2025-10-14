def odd_count(lst):
    output = []
    for string in lst:
        count = sum(1 for digit in string if int(digit) % 2 != 0)
        output.append("the number of odd elements in the string {} of the input.".format(count, string))
    return output
