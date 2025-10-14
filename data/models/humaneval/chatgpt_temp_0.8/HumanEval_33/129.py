def sort_third(l: list):
    not_divisible_by_three = [l[i] for i in range(len(l)) if i % 3 != 0]
    divisible_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    sorted_divisible_by_three = sorted(divisible_by_three)
    result = []
    index = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(sorted_divisible_by_three[index])
            index += 1
        else:
            result.append(not_divisible_by_three[i-index])
    return result
