def count_nums(arr):
    def sum_of_digits(num):
        if num == 0:
            return 0
        sign = 1 if num > 0 else -1
        num *= sign
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum * sign

    count = 0
    for num in arr:
        if sum_of_digits(num) != 0:
            count += 1
    return count
