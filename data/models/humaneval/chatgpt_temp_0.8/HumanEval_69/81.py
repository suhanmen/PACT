def search(lst):
    # Create a dictionary with the frequency of each integer in the list
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Find the greatest integer that meets the conditions
    greatest = -1
    for num, frequency in freq.items():
        if num > 0 and frequency >= num:
            greatest = max(greatest, num)

    return greatest
