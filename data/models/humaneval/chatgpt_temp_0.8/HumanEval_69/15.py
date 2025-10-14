python
def search(lst):
    # create a dictionary to store the frequency of each integer in the list
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # loop through the dictionary and find the greatest integer that meets the condition
    result = -1
    for num in freq:
        if freq[num] >= num and num > result:
            result = num
    
    return result
