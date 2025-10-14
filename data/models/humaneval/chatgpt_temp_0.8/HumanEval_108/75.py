def count_nums(arr):
    def get_digit_sum(num):
        if num == 0:
            return 0
        elif num > 0:
            return sum(int(digit) for digit in str(num))
        else:
            return -1 * sum(int(digit) for digit in str(abs(num)))

    count = 0
    for num in arr:
        if get_digit_sum(num) > 0:
            count += 1
    return count
