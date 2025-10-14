def count_nums(arr):
    def sum_digits(n):
        """
        Helper function to sum the digits of a number.
        """
        return sum([int(d) for d in str(abs(n))])
    
    count = 0
    for num in arr:
        if num < 0:
            digits = [int(d) for d in str(num)[1:]]
            digits[0] *= -1
            if sum(digits) > 0:
                count += 1
        else:
            if sum_digits(num) > 0:
                count += 1
    return count
