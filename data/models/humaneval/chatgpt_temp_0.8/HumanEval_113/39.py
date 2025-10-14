def odd_count(lst):
    output = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 == 1:
                count += 1
        output.append("the number of odd elements in the string {} of the input.".format(count, string))
    return output
