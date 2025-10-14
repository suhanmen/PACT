def count_nums(arr):
    def sum_digits(num):
        """
        Helper function to calculate the sum of digits of a number
        """
        num_str = str(num)
        if num_str[0] == '-':
            return -sum(int(digit) for digit in num_str[1:])
        else:
            return sum(int(digit) for digit in num_str)

    count = 0
    for num in arr:
        if sum_digits(num) > 0:
            count += 1
    return count
