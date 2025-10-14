def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # We can only make an array palindromic if we have at most one odd frequency number.
    # First we count the frequency of each number in the array.
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # We count how many numbers have odd frequency.
    odd_freq_count = 0
    for count in freq.values():
        if count % 2 == 1:
            odd_freq_count += 1
    
    # If we have more than one number with odd frequency, we cannot make the array palindromic.
    if odd_freq_count > 1:
        return -1
    
    # Otherwise, we can make the array palindromic by changing all numbers with odd frequency to the most common number.
    most_common_num = max(freq, key=freq.get)
    changes_needed = 0
    for num in arr:
        if num != most_common_num:
            changes_needed += 1
    
    return changes_needed // 2
