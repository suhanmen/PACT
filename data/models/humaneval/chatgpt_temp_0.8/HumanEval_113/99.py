def odd_count(lst):
    output = []
    for string in lst:
        odd_count = 0
        for char in string:
            if int(char) % 2 == 1:
                odd_count += 1
        output.append("the number of odd elements in the string {} of the input.".format(odd_count))
    return output
