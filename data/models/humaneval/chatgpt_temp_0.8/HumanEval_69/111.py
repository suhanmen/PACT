def search(lst):
    # create a dictionary to store frequency of each integer in the list
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # iterate over the dictionary to find the greatest integer that satisfies the condition
    greatest = -1
    for num, f in freq.items():
        if num > 0 and f >= num and num > greatest:
            greatest = num
    
    return greatest
