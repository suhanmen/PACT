def odd_count(lst):
    result = []
    for string in lst:
        odd_count = len([char for char in string if int(char) % 2 != 0])
        result.append("the number of odd elements in the string {} of the input.".format(odd_count, string))
    return result
