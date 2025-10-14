def odd_count(lst):
    output = []
    for string in lst:
        odd_count = sum(int(digit) % 2 == 1 for digit in string)
        output.append(f"the number of odd elements in the string {string} of the input.")
    return output
