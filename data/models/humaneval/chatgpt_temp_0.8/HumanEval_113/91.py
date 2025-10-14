def odd_count(lst):
    result = []
    for string in lst:
        count = len([digit for digit in string if int(digit) % 2 == 1])
        result.append(f"the number of odd elements {count}n the str{string} of the {lst.index(string)+1}nput.")
    return result
