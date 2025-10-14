def search(lst):
    counts = {}  # create an empty dictionary to store the frequency of each value in the list
    for num in lst:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_num = -1  # initialize the max_num variable to -1
    for num, count in counts.items():
        if num > 0 and count >= num and num > max_num:
            max_num = num
    return max_num
