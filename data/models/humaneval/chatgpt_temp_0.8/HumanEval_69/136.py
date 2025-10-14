def search(lst):
    # Create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Iterate through the dictionary to find the greatest integer that meets the condition
    max_num = -1
    for num, f in freq.items():
        if num > max_num and f >= num:
            max_num = num

    return max_num
