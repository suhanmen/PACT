def count_nums(arr):
    def sum_of_digits(n):
        return sum(int(i) for i in str(abs(n)))
    
    return len([n for n in arr if sum_of_digits(n) > 0])
