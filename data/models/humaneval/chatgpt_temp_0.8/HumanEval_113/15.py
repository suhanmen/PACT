def odd_count(lst):
    output = []
    for string in lst:
        count = sum([1 for char in string if int(char) % 2 != 0])
        output.append("the number of odd elements in the string {} of the input.".format(count))
    return output
