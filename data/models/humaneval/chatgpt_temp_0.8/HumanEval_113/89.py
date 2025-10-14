def odd_count(lst):
    output = []
    for i in lst:
        odd_count = 0
        for digit in i:
            if int(digit) % 2 == 1:
                odd_count += 1
        output.append("the number of odd elements in the string {} of the input.".format(odd_count, i))
    return output
