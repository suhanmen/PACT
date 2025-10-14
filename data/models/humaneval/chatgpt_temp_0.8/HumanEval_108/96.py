def count_nums(arr):
    def digit_sum(num):
        sgn = -1 if num < 0 else 1
        num = abs(num)
        return sgn * sum(int(d) for d in str(num))
    
    return sum(1 for num in arr if digit_sum(num) > 0)
