python
def count_nums(arr):
    count = 0
    for num in arr:
        if num >= 0:
            num_sum = sum(int(digit) for digit in str(num))
            if num_sum > 0:
                count += 1
        else:
            first_digit = int(str(num)[0])
            num_sum = sum(int(digit) for digit in str(num)[1:])
            if (num_sum > 0) or (first_digit < 0):
                count += 1
    return count
