def search(lst):
    # create a dictionary to store the frequency of each integer
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # iterate through the dictionary and find the first integer that meets the condition
    for num, count in freq.items():
        if num > 0 and count >= num:
            return num
    
    # if no such integer exists, return -1
    return -1
