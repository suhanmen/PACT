def odd_count(lst):
    result = []
    for s in lst:
        count = sum(int(digit) % 2 == 1 for digit in s)
        message = f"the number of odd elements {count}n the str{lst.index(s)+1}ng {s} of the {lst.index(s)+1}nput."
        result.append(message)
    return result
