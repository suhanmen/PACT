python
def search(lst):
    # Create a dictionary to store the frequency of each integer
    freq = {}
    for num in lst:
        freq[num] = freq.get(num, 0) + 1

    # Iterate through the dictionary to find the greatest integer that meets the criteria
    max_int = -1
    for num, count in freq.items():
        if num > 0 and count >= num:
            max_int = max(max_int, num)

    return max_int
