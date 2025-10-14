def odd_count(lst):
    output = []
    for string in lst:
        count = 0
        for char in string:
            if int(char) % 2 == 1:
                count += 1
        output.append("the number of odd elements in the string {} of the input.".format(count))
    return output
