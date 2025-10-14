def sort_even(l: list):
    even_nums = sorted([num for idx, num in enumerate(l) if idx % 2 == 0])
    sorted_l = [even_nums.pop(0) if idx % 2 == 0 else num for idx, num in enumerate(l)]
    return sorted_l
