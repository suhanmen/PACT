def search(lst):
    # create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    # loop through the dictionary to find the greatest integer that meets the condition
    max_num = -1
    for num, count in freq.items():
        if num > 0 and count >= num:
            if num > max_num:
                max_num = num
    return max_num
