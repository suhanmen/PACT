python
def count_nums(arr):
    def sum_digits(num):
        if num == 0:
            return 0
        sgn = -1 if num < 0 else 1
        num *= sgn
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total * sgn

    count = 0
    for num in arr:
        if sum_digits(num) != 0:
            count += 1
    return count
