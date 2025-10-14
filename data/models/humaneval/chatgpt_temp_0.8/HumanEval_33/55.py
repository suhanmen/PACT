def sort_third(l: list):
    divisible_by_3 = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible_by_3 = sorted(divisible_by_3)
    result = [l[i] if i % 3 != 0 else sorted_divisible_by_3[i // 3] for i in range(len(l))]
    return result
