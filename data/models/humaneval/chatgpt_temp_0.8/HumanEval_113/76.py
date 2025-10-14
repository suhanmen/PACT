python
def odd_count(lst):
    output = []
    for string in lst:
        num_odds = len([x for x in string if int(x)%2 != 0])
        output.append(f"the number of odd elements in the string {string} of the input.")
    return output
