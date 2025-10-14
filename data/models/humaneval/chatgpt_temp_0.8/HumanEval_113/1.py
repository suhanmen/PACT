def odd_count(lst):
    result = []
    for num_string in lst:
        odd_count = 0
        for digit in num_string:
            if int(digit) % 2 == 1:
                odd_count += 1
        result.append("the number of odd elements in the string {} of the input.".format(odd_count, num_string))
    return result
