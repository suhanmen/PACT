def count_nums(arr):
    def sum_digits(num):
        res = 0
        for digit in str(num):
            if digit.isdigit():
                res += int(digit)
            elif digit == '-':
                res -= 1
        return res

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count
