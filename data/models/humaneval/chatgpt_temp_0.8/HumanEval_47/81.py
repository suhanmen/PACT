def median(l: list):
    sorted_list = sorted(l)
    length = len(sorted_list)
    middle_index = length // 2
    if length % 2 == 0:
        return (sorted_list[middle_index - 1] + sorted_list[middle_index]) / 2
    else:
        return sorted_list[middle_index]
