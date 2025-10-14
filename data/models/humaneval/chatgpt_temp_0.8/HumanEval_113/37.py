def odd_count(lst):
    result = []
    for string in lst:
        odd_count = sum(int(digit) % 2 == 1 for digit in string)
        result.append(f"the number of odd elements in the string {string} of the input.")
    return result
