def order_by_points(nums):
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    # create a list of tuples containing (num, sum_of_digits(num), index)
    tuples = [(num, sum_of_digits(num), index) for index, num in enumerate(nums)]
    # sort the list by sum_of_digits and then by index
    sorted_tuples = sorted(tuples, key=lambda x: (x[1], x[2]))
    # extract the sorted numbers from the sorted tuples
    sorted_nums = [x[0] for x in sorted_tuples]
    return sorted_nums
