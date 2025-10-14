python
def specialFilter(nums):
    count = 0
    for num in nums:
        # Check if the first and last digits are odd
        first_digit = int(str(abs(num))[0])
        last_digit = int(str(abs(num))[-1])
        if first_digit % 2 != 0 and last_digit % 2 != 0:
            # Check if the number is greater than 10
            if abs(num) > 10:
                count += 1
    return count
