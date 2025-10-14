def count_nums(arr):
    def sum_of_digits(n):
        if n == 0:
            return 0
        return n % 10 + sum_of_digits(n//10)

    count = 0
    for num in arr:
        signed_digits = sum_of_digits(abs(num)) * (-1 if num < 0 else 1)
        if signed_digits != 0:
            count += 1

    return count
