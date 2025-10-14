def sort_third(l: list):
    sorted_divisible_by_three = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    result = [l[i] if i % 3 != 0 else sorted_divisible_by_three.pop(0) for i in range(len(l))]
    return result
