def count_nums(arr):
    def get_digit_sum(num):
        digits = [int(d) for d in str(num) if d.isdigit()]
        sign = -1 if str(num)[0] == '-' else 1
        return sign * sum(digits)

    count = 0
    for num in arr:
        if get_digit_sum(num) > 0:
            count += 1
    return count
