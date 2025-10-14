def count_nums(arr):
    def digit_sum(n):
        return sum(map(int, str(abs(n))))

    return sum(1 for n in arr if digit_sum(n) > 0)

