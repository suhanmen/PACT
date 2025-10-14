def odd_count(lst):
    result = []
    for string in lst:
        odd_elements = 0
        for digit in string:
            if int(digit) % 2 == 1:
                odd_elements += 1
        result.append("the number of odd elements in the string {} of the input.".format(odd_elements, string))
    return result
