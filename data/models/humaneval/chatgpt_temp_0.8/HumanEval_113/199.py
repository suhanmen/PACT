def odd_count(lst):
    result = []
    for string in lst:
        odd_count = 0
        for digit in string:
            if int(digit) % 2 == 1:
                odd_count += 1
        result.append("the number of odd elements in the string {} of the input.".format(odd_count))
    return result
