python
def odd_count(lst):
    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                count += 1
        result.append("the number of odd elements in the string {} of the input.".format(count))
    return result
