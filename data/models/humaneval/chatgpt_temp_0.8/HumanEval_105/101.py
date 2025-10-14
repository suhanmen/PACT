def by_length(arr):
    nums = [num for num in arr if 1 <= num <= 9]
    if not nums:
        return []
    nums.sort()
    nums.reverse()
    num_names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return [num_names[num] for num in nums]
