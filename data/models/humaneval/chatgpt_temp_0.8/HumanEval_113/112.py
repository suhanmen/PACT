def odd_count(lst):
    result = []
    for s in lst:
        odd_count = len([c for c in s if int(c) % 2 != 0])
        result.append(f"the number of odd elements in the string {s} of the input.")
    return result
