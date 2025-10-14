def search(lst):
    counts = {}
    for num in lst:
        if num > 0:
            counts[num] = counts.get(num, 0) + 1
    greatest_num = -1
    for num, freq in counts.items():
        if num <= freq:
            greatest_num = max(greatest_num, num)
    return greatest_num
