def sort_third(l: list):
    divisible_by_three = []
    not_divisible_by_three = []
    for i, x in enumerate(l):
        if i % 3 == 0:
            divisible_by_three.append(x)
        else:
            not_divisible_by_three.append(x)
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = []
    j = 0
    k = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(sorted_divisible_by_three[j])
            j += 1
        else:
            result.append(not_divisible_by_three[k])
            k += 1
    return result
