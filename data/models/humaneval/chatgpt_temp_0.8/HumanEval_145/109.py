python
def order_by_points(nums):

    # function to calculate the sum of digits
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))

    # create a list of tuples containing (sum of digits, index, number)
    digits_sum_list = [(sum_of_digits(num), index, num) for index, num in enumerate(nums)]

    # sort the list based on the sum of digits and index
    digits_sum_list.sort()

    # extract the sorted numbers from the list of tuples and return
    return [num for _, _, num in digits_sum_list]
