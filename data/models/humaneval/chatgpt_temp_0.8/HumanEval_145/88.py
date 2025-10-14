def order_by_points(nums):
    # Define a helper function to calculate the sum of digits of a number
    def sum_of_digits(num):
        return sum(int(digit) for digit in str(abs(num)))
    
    # Use sorted() function with a custom key function to sort the list
    return sorted(nums, key=lambda num: (sum_of_digits(num), nums.index(num)))
