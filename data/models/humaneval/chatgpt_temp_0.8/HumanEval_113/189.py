def odd_count(lst):
    result = []
    for string in lst:
        count = 0
        for char in string:
            if int(char) % 2 == 1:
                count += 1
        result.append("the number of odd elements in the string " + string + " of the input.")
    return result
