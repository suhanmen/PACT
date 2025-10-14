def odd_count(lst):
    results = []
    for num_str in lst:
        odd_count = sum(int(digit) % 2 == 1 for digit in num_str)
        result_str = f"the number of odd elements in the string {num_str} of the input."
        results.append(result_str.replace("elements", str(odd_count)))
    return results
