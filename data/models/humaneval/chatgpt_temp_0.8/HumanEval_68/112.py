def pluck(arr):
    even_nums = []
    for i, num in enumerate(arr):
        if num % 2 == 0:
            even_nums.append([num, i])
    if not even_nums:
        return []
    else:
        even_nums.sort(key=lambda x: x[0])
        return even_nums[0]
