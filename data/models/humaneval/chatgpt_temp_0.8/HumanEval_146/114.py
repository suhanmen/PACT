def specialFilter(nums):
    result = 0
    for num in nums:
        if num > 10 and str(num)[0] in ['1', '3', '5', '7', '9'] and str(num)[-1] in ['1', '3', '5', '7', '9']:
            result += 1
    return result
