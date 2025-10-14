def search(lst):
    # Create a dictionary to keep track of the frequency of each number in the list
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Iterate through the dictionary and find the greatest integer that meets the conditions
    greatest_int = -1
    for num, freq in frequency.items():
        if num > 0 and freq >= num:
            greatest_int = max(greatest_int, num)
    
    return greatest_int
