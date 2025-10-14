def odd_count(lst):
    output = []
    for string in lst:
        odd_count = sum([int(digit) % 2 != 0 for digit in string])
        output.append(f"the number of odd elements {odd_count}n the str{lst.index(string)+1}ng of the {lst.index(string)+1}nput.")
    return output
