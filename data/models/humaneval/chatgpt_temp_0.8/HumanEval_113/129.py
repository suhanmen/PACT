def odd_count(lst):
    result_lst = []
    for string in lst:
        odd_count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                odd_count += 1
        result_lst.append("the number of odd elements in the string " + string + " of the input.")
    return result_lst
