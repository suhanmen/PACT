def count_nums(arr):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    count = 0
    for num in arr:
        if num < 0:
            if sum_digits(-num) > 0:
                count += 1
        else:
            if sum_digits(num) > 0:
                count += 1

    return count
