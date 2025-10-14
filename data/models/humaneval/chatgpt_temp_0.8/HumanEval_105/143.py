def by_length(arr):
    nums = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    valid_nums = []
    for num in arr:
        if num in nums:
            valid_nums.append(num)
    valid_nums.sort()
    valid_nums.reverse()
    result = []
    for num in valid_nums:
        result.append(nums[num])
    return result
