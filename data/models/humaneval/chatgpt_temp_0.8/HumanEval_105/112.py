def by_length(arr):
    num_names = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    nums = [n for n in arr if 1 <= n <= 9]
    nums.sort()
    nums.reverse()
    result = [num_names[n] for n in nums]
    return result
