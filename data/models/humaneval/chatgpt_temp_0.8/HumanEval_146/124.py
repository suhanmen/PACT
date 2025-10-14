def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            first = int(str(num)[0])
            last = int(str(num)[-1])
            if first % 2 != 0 and last % 2 != 0:
                count += 1
    return count
