def odd_count(lst):
    res = []
    for string in lst:
        count = 0
        for char in string:
            if int(char) % 2 != 0:
                count += 1
        res.append("the number of odd elements in the string " + string + " of the input.")
    return res
