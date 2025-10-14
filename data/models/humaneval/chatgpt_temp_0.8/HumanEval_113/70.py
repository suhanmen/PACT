def odd_count(lst):
    result = []
    for string in lst:
        odd_count = 0
        for char in string:
            if int(char) % 2 != 0:
                odd_count += 1
        output = "the number of odd elements in the string {} of the input.".format(string)
        output = output.replace("the", str(odd_count))
        output = output.replace("string", "str")
        result.append(output)
    return result
